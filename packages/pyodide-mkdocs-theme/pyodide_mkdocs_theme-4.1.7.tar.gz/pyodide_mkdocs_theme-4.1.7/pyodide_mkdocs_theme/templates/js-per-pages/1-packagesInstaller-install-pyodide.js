/*
pyodide-mkdocs-theme
Copyleft GNU GPLv3 🄯 2024 Frédéric Zinelli

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.
If not, see <https://www.gnu.org/licenses/>.
*/


import { jsLogger } from 'jsLogger'
import { PythonError, sleep } from 'functools'
import { pyodideFeatureRunCode } from '0-generic-python-snippets-pyodide'






/**Explore the user's code to find missing modules to install. If some are found, load
 * micropip (if not done yet), then install all the missing modules.
 * Also import all the packages present in runner.whiteList.
 *
 * NOTE: python libs are identified by picking into the global config, but are actually
 * loaded only if they are available in the instance property (this is to limit the
 * _SAVAGE_ unexpected installations of random packages from PyPI).
 * */
export const installPythonPackages=(function(){

  /*Things are complicated, here...:
   *
   *    * Installing packages via micropip doesn't actually import them in the environment (it
   *      works the same for custom python libs).
   *    * The theme needs to know up front what packages are missing or not, to decide when to
   *      display installation messages or not.
   *    * _Installed_ packages can be found through micropip, but not _loaded_ pythonLibs.
   *
   *    So, spotting missing packages relies on picking in sys.modules.
   *    BUT, modules actually end up there _ONLY_ if a python code actually imported them, going
   *    through `import xxx`.
   *    So far, so good. Problems arise with additional features:
   *
   *    * White lists:
   *        - their content has to be actually imported in the global scope, so that they are
   *          actually available to the user.
   *
   *    * Custom libs:
   *        - They have to be imported in pyodide _right now_, so that they end up listed in
   *          `sys.modules`.
   *        - This makes them visible as "installed" on a next import/installation attempt...
   *        - ...which may occur right after the current call because imports in terminals commands
   *          may go through env, then envTerm, and BOTH will check if an import has to be done in
   *          the terminal command.
   *
   *    * Packages with different installation and import names (ex: Pillow vs PIL):
   *        Packages whose the installation name differs from the import name have to be
   *        automatically imported for the user, so that they are usable in the "triggering" code.
   *
   *    * Exclusions:
   *        - They are not applied on env sections, so modules _can_ be installed/loaded here
   *          so they _have_ to be actually imported...
   *        - ..._BUT_ hidden inside a function, so that they do not leak in the global scope.
   *        - Then the redactor's import (from the `env` or `env_term` code itself) will determine
   *          if the module ends up in the global scope or not.
   *
   *    For those reasons, all packages that are "installed" will always be imported in a hidden
   *    scope, so that they get registered in sys.modules.
   *
   *    Since the "triggering code" (env code, user code, cmd, ...) still has to be executed, the
   *    actual visibility of the imported module is left to the redactor/user, and:
   *        - All automatic installs/imports are done in a hidden scope.
   *        - Packages of the whiteList are all imported in the global scope, whatever happens or
   *          the configuration of exclusions/sections, ...
   **/



  const featureRunner = (feature, convertOutput) => (repl=null) =>{
    let out = pyodideFeatureRunCode(feature, repl)
    if(convertOutput) out = convertOutput(out)
    return out
  }


  /**In most cases, installations will be done once only, but just in case (to avoid troubles
   * with later changes... / Without that, a script tag/load could end up loaded at each call)
   * */
  const CACHE_INSTALL = new Set()


  const asyncJsScriptCdnLoader = (name, scriptOptions)=> async ()=>{
    if(CACHE_INSTALL.has(name)) return;

    let loaded = false

    const script = document.createElement('script')
    script.addEventListener("load", function(){ loaded=true })
    for(const k in scriptOptions){
      if(k=='src') continue             // Always add last...
      script[k] = scriptOptions[k]
    }
    script.src = scriptOptions.src      // Always add last...

    document.body.appendChild(script)

    while(!loaded) await sleep(50)
    CACHE_INSTALL.add(name)
    console.log(name, 'ready')
  }






  /**IMPORTS_CONFIG type:
   *
   *      Record<string, {
   *          codeCheck: Cbk
   *          toImport:  string,      // Automatic import name (in hidden scope)
   *          toInstall: string,      // Micropip installation name
   *          post:      async Cbk,   // Callback to run to apply any kind of extra logic
   *      }>
   * */
  const IMPORTS_CONFIG = {

    PIL: {
      toInstall: "Pillow"
    },

    p5: {
      codeCheck: ()=>{
        if(/from p5\S* import/.test(currentCode)){
          throw new PythonError(
            "ImportError: Invalid p5 import.\nThe p5 module must be used as a namespace:"
            +"\n    import p5\n    p5.createCanvas(...)"
          )
        }
      },
      post: asyncJsScriptCdnLoader('p5', {
        crossorigin:    "anonymous",
        referrerpolicy: "no-referrer",
        src:            "https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.11.0/p5.min.js" ,
      })

    },

    matplotlib: {
      post: async ()=>featureRunner('pyodidePlot')()
    },

  }


  const getInstallConfigFor=(libName)=>({
    toImport:  libName,
    toInstall: libName,
    post:      async ()=>undefined,
    ...IMPORTS_CONFIG[libName] || {}
  })





  const FORBID_EXTERNALS = ['py_lib', 'pylib', 'pylibs', 'py-lib', 'py-libs']
  const PMT_TOOLS = ['p5']

  /**Extract all the packages names currently available in pyodide. */
  const getAlreadyImportedPackagesAsSet = featureRunner("alreadyImported", out=>new Set(out.split(' ')) )

  /**Rely on pyodide to analyze the code content and find the imports the user is trying to use. */
  const getWantedImports = featureRunner("wantedImports")

  // Predicate factories...:
  const isInWhiteList  = (isIn, runner) => (name) => isIn == runner.whiteList.includes(name)
  const isExcluded     = (isIn, runner) => (name) => isIn == runner.excluded.includes(name)
  const isPyPiAllowed  = (isIn, runner) => (name) => isIn == ( !runner.pypiWhite || runner.pypiWhite.includes(name) )
  const isAvailablePythonLib = (runner) => (name) =>  runner.pythonLibs.has(name) ||  PMT_TOOLS.includes(name)
  const isNotKnownPythonLib              = (name) => !CONFIG.pythonLibs.has(name) && !PMT_TOOLS.includes(name)



  let micropip, currentCode;
  const enforceImports = []   // python imports to make sure python_libs are showing up in sys.modules



  /**Routine managing the actual import logic, storing the name of the module/package
   * to import later (hidden scope).
   *
   * @returns: the actual config object.
   * */
  const importFinalizer = (name) =>{
    const conf = getInstallConfigFor(name)

    if(conf.codeCheck) conf.codeCheck(currentCode)

    const importCode = `import ${ conf.toImport }`
    enforceImports.push( importCode )
    return conf
  }


  /**Install an available custom python lib.
   * */
  const installCustomPythonLib = async (libName) => {
    jsLogger("[Installer] - Install", libName)

    const conf        = importFinalizer(libName)
    const isPmtTool   = PMT_TOOLS.includes(libName)
    const rootNoSlash = CONFIG.siteUrl.replace(/\/$/, '')
    const archive     = `${ rootNoSlash }${ isPmtTool?"/assets/javascript":"" }/${ libName }.zip`
    const zipResponse = await fetch(archive)
    const zipBinary   = await zipResponse.arrayBuffer()
    pyodide.unpackArchive(zipBinary, "zip", {extractDir: libName})
    await conf.post()
  }


  /**Install an external python package (through pyodide's default behaviors: micropip+PyPI).
   * */
  const installExternalPackage = async (libName) => {
    jsLogger("[Installer] - Install", libName)

    if(FORBID_EXTERNALS.includes(libName)){
      throw new PythonError(
        `Import of ${libName} is forbidden for security reasons.\n\nDid you mean \`import py_libs\`?`
      )
    }

    if(!micropip){
      await pyodide.loadPackage("micropip");
      micropip = pyodide.pyimport("micropip");
    }
    const conf = importFinalizer(libName)
    await micropip.install(conf.toInstall)
    await conf.post()
  }


  /**Some standard libs are available, but not already imported (like statistics, for example).
   * So a basic import is tried first.
   * Note: to NOT apply on forbidden packages!
   */
  const attemptStandardLibImports=(importableLibs)=>{
    const installNeeded = []

    for(const lib of importableLibs){
      try{
        pyodide.runPython(`
def __hack_std_import_attempt():
    import ${ lib }
__hack_std_import_attempt()
`)
      }catch(e){
        installNeeded.push(lib)
      }
    }

    if(installNeeded.length != importableLibs.length){
      pyodide.runPython(`del __hack_std_import_attempt`)
    }
    return installNeeded
  }


  const forbidIfAny = (ctx, arr, head="")=>{
    if(ctx.applyExclusionsIfAny && arr.length){
      pyodide.runPython(`ExclusionError.throw("${ arr.join(', ') }", ${ head })`)
    }
  }



  // ------------------------------------------------------------------------------



  return async (runtime, ctx)=>{
    jsLogger('[Installer] - installPythonPackages')

    const runner = runtime.runner
    const code   = ctx.code

    // Refresh globals:
    currentCode = code
    enforceImports.length = 0


    const importedModules  = getAlreadyImportedPackagesAsSet()
    const isNotImportedYet = name => !importedModules.has(name)

    const wantedLibs       = getWantedImports(code)
    const maybeUndesired   = wantedLibs.filter(isInWhiteList(false, runner))

    // Spot exclusions FIRST (otherwise attemptStandardLibImports could actually import
    // some standard libs...):
    const excluded = maybeUndesired.filter(isExcluded(true, runner))
    forbidIfAny(ctx, excluded)

    const neededLibs      = wantedLibs.concat(runner.whiteList).filter(isNotImportedYet)
    const installNeeded   = attemptStandardLibImports(neededLibs)
    const pyLibsNeeded    = installNeeded.filter(isAvailablePythonLib(runner))
    const externalsNeeded = installNeeded.filter(isNotKnownPythonLib)

    jsLogger('[Installer] - pyLibsNeeded',    pyLibsNeeded)
    jsLogger('[Installer] - externalsNeeded', externalsNeeded)
    /*
    pyLibsNeeded:
          Import names matching an available python_lib.
          Using this.pythonLibs because only the available ones can be downloaded.

    externalsNeeded:
          Imports names that will attempt installation from PyPI.
          Using CONFIG.pythonLibs so that an unavailable custom lib doesn't trigger a "savage
          install" from PyPI.
    */


    // pypiWhite restrictions only apply to external requests:
    const invalid = externalsNeeded.filter(isPyPiAllowed(false, runner))
    forbidIfAny(ctx, invalid, "'cannot install '" )


    // Actual installations:
    if(pyLibsNeeded.length || externalsNeeded.length){

      runner.giveFeedback(CONFIG.lang.installStart.msg, null)
      for(const lib of pyLibsNeeded)    await installCustomPythonLib(lib)
      for(const lib of externalsNeeded) await installExternalPackage(lib)
      runner.giveFeedback(CONFIG.lang.installDone.msg, null)
    }


    // Enforce imports of all installed modules in hidden scope to be sure they end up in
    // sys.modules (not using the auto_run decorator because it might not be already in place).
    if(enforceImports.length){
      pyodide.runPython(`
def _hack_imports():
    ${ enforceImports.join('\n    ') }
_hack_imports()
del _hack_imports`)
    }


    // Make sure white listed packages are always visible in the user's scope:
    // (DON'T filter already imported modules from the white list because they could have been
    // imported in a different scope!)
    if(runner.whiteList.length){
      pyodide.runPython( runner.whiteList.map(lib=>'import '+lib).join('\n') )
    }
  }
})()
