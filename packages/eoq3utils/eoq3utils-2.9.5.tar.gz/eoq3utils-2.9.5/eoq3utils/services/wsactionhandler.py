"""
This is a management script to configure and start services of an
EOQ3 action handler client and connect it to a domain via web socket.
The action handler registers local python scripts as actions.
Those actions are executed on domain content, if triggered by
CAL commands.
An action manager connected to the same domain beforehand is
prerequisite for the action handler to work.

See EOQ User Manual for more information: https://gitlab.com/eoq/doc

2024 Bjoern Annighoefer
"""
from .. import __version__ as version
# eoq3 imports
from eoq3 import __version__ as eoqVersion
from eoq3.config import Config
from eoq3.command import Hel
from eoq3.logger import ConsoleAndFileLogger, DEFAULT_LOGGER_LEVELS
from eoq3.util import GenerateSessionId
# action manager
from eoq3pyactions import __version__ as pyActionsVersion
from eoq3pyactions.actionhandler import ActionHandler
# web socket
from eoq3autobahnws import __version__ as autobahnWsVersion
from eoq3autobahnws.autobahnwsdomainclient import AutobahnWsDomainClient
from eoq3autobahnws.util import CreateClientSslContextForSelfSignedServerCert
# eoq cli commons
from ..cli.common import PrintCliHeader, GetCliPredefinedArguments, PrintCliArgument, ArgparseToEoqConfig, CliArgument
from .common import PrintServiceReadyMessage, ServiceMenuLoop, ShallRun, ConfigFileOpenFunc
# external imports
import configargparse #like argparse but allows for config files in addition to command line parameters
import traceback
import os
import sys
#type checking 
from typing import List, Dict, Any

def ClientSslFactory(domainFactoryArgs:Dict[str,Any]): 
    return CreateClientSslContextForSelfSignedServerCert(domainFactoryArgs["sslCertificatePem"])

def PyEoq3WebSocketActionHandler(argv:List[Any])->int:
    # get predefined commandline arguments
    argDefs = GetCliPredefinedArguments([
        'printHeader',
        'printArgs',
        'config',
        'configout',
        'connectTimeout',
        'wsHost',
        'wsPort',
        'wsPort',
        'user',
        'password',
        'enableSsl',
        'sslCertificatePem',
        'logToConsole',
        'logToFile',
        'logLevel',
        'logDir',
        'printExpectedExceptionTraces',
        'printUnexpectedExceptionTraces',
    ])
    # modify predefined arguments
    argDefs['user'].default = 'aha'
    argDefs['password'].default = 'aha9873!'
    # add custom arguments
    argDefs['actionsdir'] = CliArgument('actionsdir', 'Actions dir.', typ=str, default='./Actions',           description='The path the the directory containing the action files')
    argDefs['name']       = CliArgument('name',       'Name',         typ=str, default='eoq3actionhandlerpy', description='Multiple action handlers are possible within the same domain, but each should have a unique name')
    # use configargparse to parse the command line arguments
    parser = configargparse.ArgParser(description='An eoq3 action handler connecting via web socket to a domain. Beforehand a compatible action handler has to be connected.',default_config_files=[argDefs['config'].default] if argDefs['config'].default else [],config_file_open_func=ConfigFileOpenFunc)
    for a in argDefs.values():
        parser.add_argument('--' + a.key, metavar=a.key, type=a.typ, default=a.default, help=a.description, dest=a.key, is_config_file=a.isConfigFile)
    #read the arguments
    args = parser.parse_args(argv)
    # print header
    if(args.printHeader):
        PrintCliHeader("eoq3utils.services.wsactionhandler", version,{"eoq3": eoqVersion, "eoq3pyactions": pyActionsVersion, "eoq3autobahnws": autobahnWsVersion})
    # print args
    if(args.printArgs):
        for a in argDefs.values():
            PrintCliArgument(a, getattr(args, a.key))
    #write config file if desired
    if (args.configout):
        outPath = args.configout
        args.config = None  # remove. Otherwise, the config file path is stored, which makes no sence.
        args.configout = None  # remove. Otherwise, the config file overrides itself on being used.
        parser.write_config_file(args, [outPath])
    # create an eoq3 config structure
    config = ArgparseToEoqConfig(args)
    #initialize a session ID for the action handler
    ahaSessionId = GenerateSessionId()
    try:
        #create the domain as parallel working processes 
        print("Connecting to domain... ",end="")
        sslContextFactory = None
        sslContextFactoryArgs = {}
        if(args.enableSsl):
            sslContextFactory = ClientSslFactory
            sslContextFactoryArgs = {"sslCertificatePem" : args.sslCertificatePem}
        domain = AutobahnWsDomainClient(args.wsHost,args.wsPort,sslContextFactory=sslContextFactory,sslFactoryArgs=sslContextFactoryArgs,config=config)
        print("ready")
        #create and ...
        print("Creating Action Handler... ",end="")
        aha = ActionHandler(args.actionsdir,args.name,config)
        print("ready")
        #... connect the action manager
        print("Connecting Action Handler to domain... ",end="")
        if(args.user and args.password):
            domain.Do(Hel(args.user,args.password),ahaSessionId)
        aha.Connect(domain, ahaSessionId)
        print("ready")
        PrintServiceReadyMessage()
        ServiceMenuLoop(ShallRun(), "Action Handler running.", 'q')
        #shut down
        print("Closing Action Handler... ",end="")
        aha.Close()
        print("ok")
        print("Closing domain connection... ",end="")
        domain.Close()
        print("ok")
        print('Action Handler says goodbye!')
        return 0 #no failure
    except Exception as e:
        print("ERROR: %s"%(str(e)))
        traceback.print_exc()
        return 1 #make sure all processes are killed
        
        
'''
MAIN: Execution starts here
'''            
if __name__ == "__main__":
    code = PyEoq3WebSocketActionHandler(sys.argv[1:])
    os._exit(code)
    