'''
Can be used to send a command via the command-line to a TCP domain.
2024 Bjoern Annighoefer
'''

from eoq3.value import STR
from eoq3.command import Hel
from eoq3.config import Config
from eoq3.serializer import CreateSerializer
from eoq3.util import GenerateSessionId

from eoq3tcp.tcpdomainclient import TcpDomainClient

import argparse

'''
MAIN: Execution starts here
'''            
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Executes a command on a remote TCP domain.')
    parser.add_argument('-c','--cmd', metavar='cmd', type=str, default='GET (/*MDB)', help='The command to be executed')
    parser.add_argument('-s','--serializer', metavar='serializer', type=str, default='TXT', help='The command and result serialization')
    parser.add_argument('-t','--host', metavar='host', type=str, default='localhost', help='Host address')
    parser.add_argument('-p','--port', metavar='port', type=int, default=6141, help='Host port')
    parser.add_argument('-u','--user', metavar='user', type=str, default=None, help='If given, use this user to login', dest='user')
    parser.add_argument('-w','--pw', metavar='pw', type=str, default=None, help='Credential to authorize the user', dest='pw')
    args = parser.parse_args()
     
    config = Config()
    config.remoteCmdSerializer = "TXT"
    config.remoteRawLogging = True
    #convert the command
    serializer = CreateSerializer(args.serializer)
    cmd = serializer.DesCmd(args.cmd)
    
    sessionId = None
    #create client
    domain = TcpDomainClient(args.host,args.port,2**20,b'\x00',config)
    try:
    #login if desired
        if(args.user and args.pw):
            sessionId = GenerateSessionId()
            domain.Do(Hel(STR(args.user),STR(args.pw)),sessionId)
        #issue the command
        res = domain.Do(cmd,sessionId)
        resStr = serializer.SerVal(res)
        print(resStr,end="")
    finally:
        #close domain
        domain.Close()
        
    