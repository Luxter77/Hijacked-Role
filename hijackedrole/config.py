import argcomplete
import argparse
import asyncio
import os
import pickle
import sys

from discord import User
from discord.ext.commands import Bot

from hijackedrole.game.stuff import CampaingDB, PlayerDB
from hijackedrole.logger import logMe

class CONF0:
    '''IIII'm gonna swwwiiiing from a chandelieeeeeeer'''
    def __init__(self, CommandPrefix: str, TOKEN: str, DB_PATH: str, debug: int,
                 logAdmin: User = None, logChan: str = None, initArgs = None) -> None:
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
    parser.add_argument("-D", "--db", type=_path, help="Bot Data directory",
                        default=os.path.join(_get_def_doc(), 'Hijacked-Role'))
    parser.add_argument("-V", "--debug", type=int,
                        help="Discord text channel(id) where to dump logs")
    parser.add_argument("-n", "--puke", action="store_true",
                        help="Prints configuration in file and returns (does nothing else)")
    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    os.makedirs(args.db, exist_ok=True)
    if (args.puke):
        if (os.path.isfile(os.path.join(args.db, 'config.pkl'))):
            print(
                ('TOKEN\t\t=>\t{}\n' + 'Prefix\t=>\t{}\n' + 'Data Dir\t=>\t{}\n' + 'Debug\t=>\t{}')
                .format(*pickle.load(open(os.path.join(args.db, 'config.pkl'), "wb"))))
            sys.exit(0)
        else:
            print("My stomach's empty, I can't puke")
            sys.exit(1)

    if not (os.path.isfile(os.path.join(args.db, 'config.pkl'))):
        if not (args.TOKEN):
            print("--> A Bot token is required on first launch <--")
            parser.print_usage()
            sys.exit(1)
        else:
            pickle.dump(tuple((args.TOKEN, args.prefix, args.db, args.debug)),
                        open(os.path.join(args.db, 'config.pkl'), "wb"))
            config = CONF0(TOKEN=args.TOKEN,
                           CommandPrefix=args.prefix,
                           DB_PATH=args.db,
                           debug=args.debug)
    else:
        if not(args.TOKEN):
            config = CONF0(*pickle.load(open(os.path.join(args.db, 'config.pkl'), 'rb')),
                           initArgs=args)
        else:
            pickle.dump(tuple((args.TOKEN, args.prefix, args.db, args.debug)),
                        open(os.path.join(args.db, 'config.pkl'), "wb"))
            config = CONF0(TOKEN=args.TOKEN,
                           CommandPrefix=args.prefix,
                           DB_PATH=args.db,
                           debug=args.debug,
                           initArgs=args)
    return(config)

async def getPDB() -> PlayerDB:
    try:
        global config
        return(PlayerDB(pickle.load(open(os.path.join(config.args.db, 'PDB.pkl'), 'rb'))))
    except Exception as Err_:
        await logMe(Err_)
        return(PlayerDB())

async def getCDB() -> CampaingDB:
    try:
        global config
        return(pickle.load(open(os.path.join(config.args.db, 'CDB.pkl'), 'rb')))
    except Exception as Err_:
        await logMe(Err_)
        return(CampaingDB())
