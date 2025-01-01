"""
 Common functions used for EOQ CLI modules

 Bjoern Annighoefer 2024
"""

from eoq3.config import Config
from eoq3.logger import DEFAULT_LOGGER_LEVELS

from importlib.resources import files, as_file # for internal resources
from typing import Any, Dict, List, Tuple


def GetInModuleFileAbsPath(moduleName:str, innerPath:str, fileName:str)->str:
    """Returns the absolute path for a file delivered in a module
    """
    filePath = None
    with as_file(files(moduleName).joinpath(innerPath).joinpath(fileName)) as moduleFile:
        filePath = str(moduleFile.absolute())
    return filePath

class CliArgument:
    """A class to define a command line argument used by eoq3 CLI modules.
    This seperate class enables an easy conversion to argparse arguments or
    configargparse arguments.
    It also enables to reuse arguments in different CLI modules.
    """
    def __init__(self, key:str, name:str, short:str=None, description:str=None, required:bool=False, typ:any=str, default:Any=None, isSecret:bool=False, isConfigFile:bool=False):
        self.key:str = key #key to be used in the command line, i.e. --key
        self.name:str = name #full text name of the argument
        self.short:str = short #one char key (optional) for the command line, i.e. -k
        self.description:str = description #
        self.required:bool = required
        self.typ:str = typ #str,int
        self.default:Any = default
        self.isSecret:bool = isSecret #if true, the value is not printed
        self.isConfigFile:bool = isConfigFile #if true, the value is a path to a config file

CLI_ARGS_REGISTRY:Dict[str,CliArgument] = {} # a registry for predefined CLI arguments

def RegisterCliArgument(key:str, name:str, short:str=None, description:str=None, required:bool=False, typ:str=str, default:Any=None, isSecret:bool=False, isConfigFile:bool=False):
    CLI_ARGS_REGISTRY[key] = CliArgument(key, name, short, description, required, typ, default, isSecret, isConfigFile)

def GetCliPredefinedArguments(keys:List[str])->Dict[str,CliArgument]:
    """Returns a dictionary with the predefined arguments if existing.
    If a key does not exist in the predefined ones, an exception is raised.
    """
    return {k:CLI_ARGS_REGISTRY[k] for k in keys}

def PrintCliHeader(name:str=None,version:str=None,subVersions:Dict[str,str]=None,showLicense:bool=True,showCopyRight:bool=True, author:str='Bjoern Annighoefer'):
    """Default header printout for all pyeoq3 CLI modules.
    Prints the name, version, subversions, license and copy right.
    """
    print('************ pyeoq3 ************')
    if(name):
        print('%s:'%(name),end='')
    if(version):
        print('%s'%(version))
    if(subVersions):
        print("(%s)"%(", ".join(["%s:%s"%(k,v) for k,v in subVersions.items()])))
    if(showCopyRight):
        print("Copyright (c) 2022 %s"%(author))
    if(showLicense):
        print("MIT license - no warranty")
    print('********************************')

def PrintCliArgument(ca:CliArgument,value:Any=None,allign:int=20):
    """Prints a cli argument with its value
    If the value is a secret, it is masked by stars
    """
    if(ca.isSecret and None != value):
        value = '********'
    elif(str==type(value)):
        value = "'%s'"%(value)
    nl = len(ca.name)
    print('%s:%s%s'%(ca.name,"".join([" " for i in range(allign-nl)]),str(value)))

def _GetLoggerLevelsByNumber(l:int):
    """Internal function to convert the logger levels from a single number.
    0 is silent, 1 is error, 2 is warning, 3 is info, 4 is debug.
    """
    logLevels = DEFAULT_LOGGER_LEVELS.L0_SILENT
    if(0 == l):
        logLevels = DEFAULT_LOGGER_LEVELS.L0_SILENT
    elif(1 == l):
        logLevels = DEFAULT_LOGGER_LEVELS.L1_ERROR
    elif(2 == l):
        logLevels = DEFAULT_LOGGER_LEVELS.L2_WARNING
    elif(3 == l):
        logLevels = DEFAULT_LOGGER_LEVELS.L3_INFO
    elif(4 == l):
        logLevels = DEFAULT_LOGGER_LEVELS.L4_DEBUG
    else:
        raise EOQ_ERROR_INVALID_VALUE('Invalid value %d for log level'%(l))
    return logLevels

def _GetLoggerAndInitArgs(logToConsole, logToFile, logDir)->Tuple[str,Dict[str,Any]]:
    """Internal function to retrieve the logger and its init arguments
    based on the logToConsole and logToFile args.
    """
    if(logToConsole and logToFile):
        return "CFL", {"logDir":logDir, "prefix":""}
    elif(logToConsole):
        return "CON", {}
    elif(logToFile):
        return "FIL", {"logDir":logDir, "prefix":""}
    else:
        return "NOL", {}

def ArgparseToEoqConfig(args:Any)->Config:
    """Converts argparse arguments to an EOQ config
    All fields relevant for the EOQ config must be present in the argparse arguments,i.e.
    logToConsole, logToFile, logDir, logLevel, printExpectedExceptionTraces, printUnexpectedExceptionTraces
    connectTimeout
    """
    # initialize EOQ config
    config = Config()
    # determine loglevel
    config.activeLogLevels = _GetLoggerLevelsByNumber(args.logLevel)
    config.logger, config.loggerInitArgs = _GetLoggerAndInitArgs(args.logToConsole, args.logToFile, args.logDir)
    config.printExpectedExceptionTraces = args.printExpectedExceptionTraces
    config.printUnexpectedExceptionTraces = args.printUnexpectedExceptionTraces
    config.connectTimeout = args.connectTimeout  # reduce timeout to 2 seconds #TODO? make this configurable
    return config

def none_or_str(value):
    """Fake type for argparse to allow for None values for strings
    """
    if value == 'None':
        return None
    return value

### REGISTER COMMON CLI ARGUMENTS ###
# Verbosity
RegisterCliArgument('printHeader',            "Print header",         typ=int,         default=1,       description='Show the header (1=show, 0=hide)')
RegisterCliArgument('printArgs',              "Print arg",            typ=int,         default=1,       description='Show list of arguments (1=show, 0=hide)')
# User
RegisterCliArgument('user',                   'User',                 typ=none_or_str, default=None,    description='If given, this user is used for accessing the domain')
RegisterCliArgument('password',               'Password',             typ=none_or_str, default=None,    description='If given and user is given, this password is used for accessing the domain', isSecret=True)
# Logging
RegisterCliArgument('logToConsole',           "Console log",          typ=int,         default=0,       description='Print log messages in the console? (0=no, 1=yes)')
RegisterCliArgument('logToFile',              "File log",             typ=int,         default=1,       description='Print log messages in log files? (0=no, 1=yes)')
RegisterCliArgument('logLevel',               "log levels",           typ=int,         default=2,       description='The verboseness of logging (0=silent, 1=error, 2=warning, 3=info, 4=debug)')
RegisterCliArgument('logDir',                 "Log path",             typ=str,         default='./log', description='Destination folder for log files')
RegisterCliArgument('printExpectedExceptionTraces',   "Trace known",  typ=int,         default=0,       description='Print Python trace for expected exceptions')
RegisterCliArgument('printUnexpectedExceptionTraces', "Trace unknown",typ=int,         default=1,       description='Print Python trace output for unexpected exceptions')