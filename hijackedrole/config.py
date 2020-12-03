import argcomplete
import argparse
import asyncio
import os
import pickle
import sys

from discord import User
from discord.ext.commands import Bot

from hijackedrole.game import CampaingDB, PlayerDB

'''
class DBAuth:
   def __init__(self uri: str = r'localhost', user: str = r'HijackedRole', password: str = r'postgre'):
      self.uri, self.user, self.password = uri, user, password
'''


class CONF0:
    '''IIII'm gonna swwwiiiing from a chandelieeeeeeer'''
    def __init__(self, CommandPrefix: str, TOKEN: str, DB_PATH: str, debug: int,
                 logAdmin: User = None, logChan: str = None, initArgs=None) -> None:
        self.CommandPrefix = CommandPrefix
        self.DB_PATH = DB_PATH
        self.TOKEN = TOKEN
        self.debug = debug
        self.LogAdmin = set(logAdmin) if (logAdmin) else set()
        self.LogChan = set(logChan) if (logChan) else set()
        self.args = initArgs

def _path(string) -> str:
    'Check if string is a directory'
    os.makedirs(string, exist_ok=True)
    if (os.path.isdir(string)):
        return (string)
    raise (NotADirectoryError(string))

def _get_def_doc() -> str:
    'Get Documents folder'
    if (os.name == 'nt'):
        import ctypes.wintypes
        buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, 5, None, 0, buf)
        return (str(buf.value))
    else:
        import subprocess
        return(
            subprocess.check_output(["xdg-user-dir", "DOCUMENTS"], universal_newlines=True).strip()
        )

def getConfig() -> CONF0:
    parser = argparse.ArgumentParser(description='Configures Hijacked-Role')
    parser.add_argument("-T", "--TOKEN", type=str, help="Discord API bot TOKEN",)
    parser.add_argument("-P", "--prefix", type=str, help="Bot command prefix", default="$")
    parser.add_argument("-D", "--dbDir", type=_path, help="Bot Data directory", default=os.path.join(_get_def_doc(), 'Hijacked-Role'))
    parser.add_argument("-V", "--debug", type=int, help="Discord text channel(id) where to dump logs")

    parser.add_argument("-n", "--puke", action="store_true", help="Prints configuration in file and returns (does nothing else)")

    parser.add_argument("--dbURI",  type=str, help="Squirrel Remote Database URI.",     default="localhost")
    parser.add_argument("--dbUser", type=str, help="Squirrel Database URI.",     default="Hijacked-Role")
    parser.add_argument("--dbPass", type=str, help="Database Password", default="postgre")

    argcomplete.autocomplete(parser)

    args = parser.parse_args()

    os.makedirs(args.D, exist_ok=True)
    if (args.puke):
        if (os.path.isfile(os.path.join(args.D, 'config.pkl'))):
            print(
                ('TOKEN\t\t=>\t{}\n' + 'Prefix\t=>\t{}\n' + 'Data Dir\t=>\t{}\n' + 'Debug\t=>\t{}')
                .format(*pickle.load(open(os.path.join(args.D, 'config.pkl'), "wb"))))
            sys.exit(0)
        else:
            print("My stomach's empty, I can't puke")
            sys.exit(1)

    if not (os.path.isfile(os.path.join(args.D, 'config.pkl'))):
        if not (args.T):
            print("--> A Bot token is required on first launch <--")
            parser.print_usage()
            sys.exit(1)
        else:
            pickle.dump(tuple((args.T, args.P, args.D, args.V)),
                        open(os.path.join(args.D, 'config.pkl'), "wb"))
            config = CONF0(TOKEN=args.T,
                           CommandPrefix=args.P,
                           DB_PATH=args.D,
                           debug=args.V)
    else:
        if not(args.T):
            config = CONF0(*pickle.load(open(os.path.join(args.D, 'config.pkl'), 'rb')),
                           initArgs=args)
        else:
            pickle.dump(tuple((args.T, args.P, args.D, args.V)),
                        open(os.path.join(args.D, 'config.pkl'), "wb"))
            config = CONF0(TOKEN=args.T,
                           CommandPrefix=args.P,
                           DB_PATH=args.D,
                           debug=args.V,
                           initArgs=args)
    return(config)

async def getPDB() -> PlayerDB:
    try:
        global config
        return(PlayerDB(pickle.load(open(os.path.join(config.args.D, 'PDB.pkl'), 'rb'))))
    except Exception as Err_:
        return(PlayerDB())

'''
async def getCDB() -> CampaingDB:
    try:
        global config

    except Exception:
        pass
'''

async def getCDB() -> CampaingDB:
    try:
        global config
        return(pickle.load(open(os.path.join(config.args.D, 'CDB.pkl'), 'rb')))
    except Exception as Err_:
        return(CampaingDB())
