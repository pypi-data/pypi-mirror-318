"""
This is a management script to configure and start services of an
EOQ3 action manager client and connect it to a domain via web socket.
The action manager extends the domain with the ability to register and execute
custom actions.

See EOQ User Manual for more information: https://gitlab.com/eoq/doc

2024 Bjoern Annighoefer
"""

from .. import __version__ as version
# eoq3 imports
from eoq3 import __version__ as eoqVersion
from eoq3.command import Hel
from eoq3.util import GenerateSessionId
# action manager
from eoq3pyactions import __version__ as pyActionsVersion
from eoq3pyactions.actionmanager import ActionManager
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

def PyEoq3WebSocketActionManager(argv:List[Any])->int:
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
    argDefs['user'].default = 'ama'
    argDefs['password'].default = 'ama0948&'
    # use configargparse to parse the command line arguments
    parser = configargparse.ArgParser(description='An eoq3 action manager connecting via web socket to a domain.',default_config_files=[argDefs['config'].default] if argDefs['config'].default else [],config_file_open_func=ConfigFileOpenFunc)
    for a in argDefs.values():
        parser.add_argument('--' + a.key, metavar=a.key, type=a.typ, default=a.default, help=a.description, dest=a.key, is_config_file=a.isConfigFile)
    #read the arguments
    args = parser.parse_args(argv)
    # print header
    if(args.printHeader):
        PrintCliHeader("eoq3utils.services.wsactionmanager", version,{"eoq3": eoqVersion, "eoq3pyactions": pyActionsVersion, "eoq3autobahnws": autobahnWsVersion})
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
    #initialize a session ID for the action manager
    amaSessionId = GenerateSessionId()
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
        print("Creating Action Manager... ",end="")
        ama = ActionManager(config)
        print("ready")
        #... connect the action manager
        print("Connecting Action Manager to domain... ",end="")
        if(args.user and args.password):
            domain.Do(Hel(args.user,args.password),amaSessionId)
        ama.Connect(domain, amaSessionId)
        print("ready")
        PrintServiceReadyMessage()
        ServiceMenuLoop(ShallRun(), "Action Manager running.", 'q')
        #shut down 
        print("Closing Action Manager... ",end="")
        ama.Close()
        print("ok")
        print("Closing domain connection... ",end="")
        domain.Close()
        print("ok")
        print('Action Manager says goodbye!')
        return 0 #no failure
    except Exception as e:
        print("ERROR: %s"%(str(e)))
        traceback.print_exc()
        return 1 #make sure all processes are killed


'''
MAIN: Execution starts here
'''            
if __name__ == "__main__":
    code = PyEoq3WebSocketActionManager(sys.argv[1:])
    os._exit(code)
    