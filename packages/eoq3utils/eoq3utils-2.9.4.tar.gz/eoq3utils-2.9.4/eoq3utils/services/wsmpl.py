"""
This is a management script to configure and start services of an EOQ3 model persistence layer (MPL) client
and connect it to a domain via web socket.

See EOQ User Manual for more information: https://gitlab.com/eoq/doc

2024 Bjoern Annighoefer
"""
from .. import __version__ as version
# eoq
from eoq3 import __version__ as eoqVersion
from eoq3.config import Config
from eoq3.command import Hel
from eoq3.logger import ConsoleAndFileLogger, DEFAULT_LOGGER_LEVELS
from eoq3.serializer import TextSerializer
from eoq3.util import GenerateSessionId
# mpl
from eoq3pyecorempl import __version__ as pyEcoreMplVersion
from eoq3pyecorempl import PyEcoreWorkspaceMpl
from eoq3pyecoreutils.pyecorepatch import EnableEObjectAnnotationsPatch
# web socket
from eoq3autobahnws import __version__ as autobahnWsVersion
from eoq3autobahnws.autobahnwsdomainclient import AutobahnWsDomainClient
from eoq3autobahnws.util import CreateClientSslContextForSelfSignedServerCert
# eoq cli commons
from ..cli.common import PrintCliHeader, GetCliPredefinedArguments, PrintCliArgument, ArgparseToEoqConfig, CliArgument
from .common import PrintServiceReadyMessage, ServiceMenuLoop, ShallRun, ConfigFileOpenFunc
# external imports
from timeit import default_timer as timer #used to time the command's execution time.
import configargparse #like argparse but allows for config files in addition to command line parameters
import traceback
import os
import sys
# type annotations
from typing import List, Dict, Any


### SSL FACTORIES ###

def ClientSslFactory(domainFactoryArgs:Dict[str,Any]): 
    return CreateClientSslContextForSelfSignedServerCert(domainFactoryArgs["sslCertificatePem"])

def PyEoq3WebSocketMpl(argv:List[Any])->int:
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
        'enableEObjectAnnotationsPatch',
        'logToConsole',
        'logToFile',
        'logLevel',
        'logDir',
        'printExpectedExceptionTraces',
        'printUnexpectedExceptionTraces',
    ])
    # modify predefined arguments
    argDefs['user'].default='mpl'
    argDefs['password'].default='mpl6333!'
    # add custom arguments
    argDefs['workspace']          = CliArgument('workspace',          'Workspace',        typ=str, default='./Workspace', description='The path the the directory containing the model files')
    argDefs['shallLoad']          = CliArgument('shallLoad',          'Shall load',       typ=int, default=1,             description='Upload the content of the workspace in the domain (0=no, 1=yes)')
    argDefs['shallMonitor']       = CliArgument('shallMonitor',       'Shall monitor',    typ=int, default=1,             description='Listens to changes in the domain and updates the local workspace accordingly. Requires upload to be enabled. (0=no, 1=yes)')
    argDefs['shallStore']         = CliArgument('shallStore',         'Shall store',      typ=int, default=0,             description='Download the content of the domain to the local workspace. Overrides the workspace! (NOT IMPLEMENTED) (0=no, 1=yes)')
    argDefs['containingElement']  = CliArgument('containingElement',  'Containing elem.', typ=str, default='(/*MDB)',     description='The query to the object that holds the root of the workspace in the domain')
    argDefs['containingFeature']  = CliArgument('containingFeature',  'Containing feat.', typ=str, default='*ROOT',       description='The feature name that contains the workspace root.')
    # use configargparse to parse the command line arguments
    parser = configargparse.ArgParser(description='An eoq3 model persistence layer connecting via web socket to a domain.',default_config_files=[argDefs['config'].default] if argDefs['config'].default else [],config_file_open_func=ConfigFileOpenFunc)
    for a in argDefs.values():
        parser.add_argument('--' + a.key, metavar=a.key, type=a.typ, default=a.default, help=a.description, dest=a.key, is_config_file=a.isConfigFile)
    #read the arguments
    args = parser.parse_args(argv)
    # print header
    if(args.printHeader):
        PrintCliHeader("eoq3utils.services.wsmpl", version,{"eoq3": eoqVersion, "pyEcoreMdbVersion": pyEcoreMplVersion, "eoq3autobahnws": autobahnWsVersion})
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
    #check containing element format
    serializer = TextSerializer()
    try:
        containerQry = serializer.DesQry(args.containingElement)
    except Exception as e:
        raise ValueError("Containing feature has wrong format: %s"%(str(e)))
    config = ArgparseToEoqConfig(args)
    #initialize a session ID for the access controller
    mplSession = GenerateSessionId()
    try:
        #create the domain as parallel working processes 
        print("Connecting to domain... ",end="")
        sslContextFactory = None
        sslContextFactoryArgs = {}
        if(args.enableSsl):
            sslContextFactory = ClientSslFactory
            sslContextFactoryArgs = {"sslCertificatePem" : args.sslCertificatePem}
        if(args.enableEObjectAnnotationsPatch):
            EnableEObjectAnnotationsPatch()
        domain = AutobahnWsDomainClient(args.wsHost,args.wsPort,sslContextFactory=sslContextFactory,sslFactoryArgs=sslContextFactoryArgs,config=config)
        print("ready")
        #create and start the web socket server
        print("Creating MPL... ",end="")
        mpl = PyEcoreWorkspaceMpl(args.workspace,config=config) #./Meta must contain oaam.ecore
        print("ready")
        workspaceObj = None
        #load workspace to domain if desired
        if(args.shallLoad):
            start = timer()
            print("Uploading workspace...   0%",end="")
            mpl.Load()
            #connecting to domain
            progressHandler = lambda p: print("\b\b\b\b%3d%%"%(p),end="")
            if(args.user and args.password):
                domain.Do(Hel(args.user,args.password),mplSession)
                workspaceObj = mpl.Connect(domain,containerQry,args.containingFeature,mplSession,trackDomainChanges=args.shallMonitor, progressCallback=progressHandler)
            else:
                workspaceObj = mpl.Connect(domain,containerQry,args.containingFeature,trackDomainChanges=args.shallMonitor, progressCallback=progressHandler)
            end = timer()
            print(" complete (%.2f s)"%(end-start))
            print("The workspace root is %s."%(serializer.SerVal(workspaceObj)))
        print("MPL ready.")
        PrintServiceReadyMessage()
        #stay in monitor loop if desired
        if(args.shallMonitor):
            ServiceMenuLoop(ShallRun(), "Monitoring domain changes.",'q')
        #download domain if desired
        if(args.shallStore):
            start = timer()
            print("Downloading workspace... ",end="")
            mpl.Store() #TODO: download is not implemented
            end = timer()
            print("complete (%.2f s)"%(end-start))
        #shut down 
        print("Closing MPL... ",end="")
        mpl.Close()
        print("ok")
        print("Closing domain connection... ",end="")
        domain.Close()
        print("ok")
        print('MPL says goodbye!')
        return 0 #no failure
    except Exception as e:
        print("ERROR: %s"%(str(e)))
        traceback.print_exc()
        return 1 #make sure all processes are killed
        
        
'''
MAIN: Execution starts here
'''            
if __name__ == "__main__":
    code = PyEoq3WebSocketMpl(sys.argv[1:])
    os._exit(code)
    