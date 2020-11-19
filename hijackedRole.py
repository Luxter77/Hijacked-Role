#!/usr/bin/env python3
# coding: utf-8
from tqdm.asyncio import tqdm as asynctqdm
from discord.ext import commands
from discord.ext import buttons
from tqdm.auto import tqdm

import datetime as dt
import traceback
import argparse
import discord
import asyncio
import random
import pickle
import glob
import sys
import os
import re

class CONF0():
    '''IIII'm gonna swwwiiii from a chandelieeeeeeer'''

    def __init__(self, CommandPrefix: str, TOKEN: str, DB_PATH: str, debug: int, 
                 logAdmin: discord.User = None, logChan: discord.channel = None):
        self.CommandPrefix	=	CommandPrefix
        self.DB_PATH		=	DB_PATH
        self.TOKEN			=	TOKEN
        self.debug			=	debug
        self.LogAdmin		=	set(logAdmin)	if (logAdmin)	else set()
        self.LogChan		=	set(logChan)	if (logChan)	else set()

    def add_LogChan(self, Chan: discord.channel):
        self.LogChan.add(Chan)

    def del_LogChan(self, Chan: discord.channel):
        self.LogChan.remove(Chan)

    def add_LogAdmin(self, Admin: discord.User):
        self.LogAdmin.add(Admin)

    def del_LogAdmin(self, Admin: discord.User):
        self.LogAdmin.remove(Admin)


# Why do I keep doing this to myself
def _path(string):
    'Check if string is a directory'
    os.makedirs(string, exist_ok=True)
    if (os.path.isdir(string)):
        return (string)
    raise (NotADirectoryError(string))


def _get_def_doc():
    'Get Documents folder'
    if (os.name == 'nt'):
        import ctypes.wintypes
        buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, 5, None, 0, buf)
        return (str(buf.value))
    else:
        import subprocess
        return (subprocess.check_output(["xdg-user-dir", "DOCUMENTS"], universal_newlines=True).strip())


parser = argparse.ArgumentParser(description='Configures Hijacked-Role')

parser.add_argument("-T",	"--TOKEN",	type=str,			help="Discord API bot TOKEN",)
parser.add_argument("-P",	"--prefix",	type=str,			help="Bot command prefix",
                    default="$")
parser.add_argument("-D",	"--db",		type=_path,			help="Bot Data directory",
                    default=os.path.join(_get_def_doc(), 'Hijacked-Role'))
parser.add_argument("-V",	"--debug",	type=int,
                    help="Discord channel(id) where to dump logs")
parser.add_argument("-n",	"--puke",	action="store_true",
                    help="Prints configuration in file and returns (does nothing else)")

args = parser.parse_args()

os.makedirs(args.db, exist_ok=True)
if (args.puke):
    if (os.path.isfile(os.path.join(args.db, 'config.pkl'))):
        print(('TOKEN\t\t=>\t{}\n' + 'Prefix\t=>\t{}\n' + 'Data Dir\t=>\t{}\n' + 'Debug\t=>\t{}').format(*pickle.load(open(os.path.join(args.db, 'config.pkl'), "wb"))))
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
        config = CONF0(*pickle.load(open(os.path.join(args.db, 'config.pkl'), 'rb')))
    else:
        pickle.dump(tuple((args.TOKEN, args.prefix, args.db, args.debug)),
                    open(os.path.join(args.db, 'config.pkl'), "wb"))
        config = CONF0(TOKEN=args.TOKEN,
                       CommandPrefix=args.prefix,
                       DB_PATH=args.db,
                       debug=args.debug)

# HERE BE STUFF
class GameClass():
    "TODO: change classes to somethign more original"
    "TODO: Make it so there are other classes"
    "for now, just DnD classes"
    def __init__(self, name: str, dice: list, clvl: int = 1, rng: bool = True):
        self.dice = dice
        self.name = name
        self.clvl = clvl
        self.rng = rng

    def __str__(self):
        return ('<' + self.name + '>::<lvl:' + str(self.clvl) + '>')
class Barbarian(GameClass):
    name = 'barbarian'
    dice = [[1, 12], [7, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)

class Bard(GameClass):
    name = 'bard'
    dice = [[1, 8], [5, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)

class Cleric(GameClass):
    name = 'cleric'
    dice = [[1, 8], [5, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)
class Druid(GameClass):
    name = 'druid'
    dice = [[1, 8], [5, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)
class Fighter(GameClass):
    name = 'fighter'
    dice = [[1, 10], [6, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)

class Monk(GameClass):
    name = 'monk'
    dice = [[1, 8], [5, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)

class Paladin(GameClass):
    name = 'paladin'
    dice = [[1, 10], [6, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)

class Ranger(GameClass):
    name = 'ranger'
    dice = [[1, 10], [6, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)

class Rogue(GameClass):
    name = 'rogue'
    dice = [[1, 8], [5, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)

class Sorcerer(GameClass):
    name = 'sorcerer'
    dice = [[1, 6], [4, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)

class Warlock(GameClass):
    name = 'warlock'
    dice = [[1, 8], [5, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)

class Wizard(GameClass):
    name = 'wizard'
    dice = [[1, 6], [4, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)

class CharStats():
    '''
    strength		(strg): How much you strong,\n
    inteligence 	(inte): How much you think,\n
    speed			(sped): How fast you move,\n
    dexterity		(dext): How well you move,\n
    wisdom			(wisd):	How well you think,\n
    constitution	(conn):	How well you,\n
    carisma			(char): How nice you,\n
    luck 			(luck): How well you,\n
    seed			(seed): How.
    '''
    def __init__(self, strg: int = 10, inte: int = 10, sped: int = 10, dext: int = 10,
                 wisd: int = 10, conn: int = 10, char: int = 10, luck: int = 50,
                 levl: int = 1, seed: int = None):
        self.wisd, self.conn, self.char, self.luck, self.levl = wisd, conn, char, luck, levl
        self.strg, self.inte, self.sped, self.dext = strg, inte, sped, dext
        self.seed = seed if (seed) else random.randint(-65535, 65536)

    def __str__(self):
        return (
            'Stats:'			+
            '\n\tstr:\t\t\t'	+	str(self.strg) +	' How much you strong'	+
            '\n\tint:\t\t\t'	+	str(self.inte) +	' How much you think'	+
            '\n\tspd:\t\t\t'	+	str(self.sped) +	' How fast you move'	+
            '\n\tdex:\t\t\t'	+	str(self.dext) +	' How well you move'	+
            '\n\twis:\t\t\t'	+	str(self.wisd) +	' How well you think'	+
            '\n\tcon:\t\t\t'	+	str(self.conn) +	' How well you'			+
            '\n\tchr:\t\t\t'	+	str(self.char) +	' How you'				+
            '\n\tluck:\t\t\t'	+	str(self.luck) +	' How well'				+
            '\n\tlevel:\t\t\t'	+	str(self.levl) +	' How much'				+
            '\n\tmagic number:\t'	+	str(self.seed) + 	' How.'
        )

class CharState():
    'TODO: *'
    def __init__(self, MaxHP: int = 5):
        self.MaxHP		=	MaxHP
        self.HP			=	MaxHP

class GameObject():
    '''A thing that a Character can have or equip or use'''
    def __init__(self, name: str, stats: CharStats, description: str = "What title says",
                 equipable: bool = False, isequiped: bool = False, usable: bool = False,
                 isAmmo: bool = False, ammount: int = 1):
        self.name			=	name
        self.stats			=	stats
        self.description	=	description
        self.equipable		=	equipable
        self.isequiped		=	isequiped
        self.usable			=	usable
        self.isAmmo			=	isAmmo
        self.ammount		=	max(0, ammount)

    def trow(self, ammount: int = 1):
        self.ammount = max(0, self.ammount - ammount)

    def __str__(self):
        return ('<' + self.name + '>\n[ ' + str(self.description) + ' ]\n' +
                'Stats:\n' + str(self.stats) + '\n' +
                (('This object is equipable.\n') if (self.equipable) else '') +
                (('This object is usable.\n') if
                 (self.usable) else '') + (('This object is ammo.\n') if
                                           (self.equipable) else ''))

class Character():
    """Playable Character, OC, if you will"""
    def __init__(self, name: str, alighn: list = [], stats: CharStats = None,
                 gaem_class: GameClass = None):
        self.name			=	name
        self.alighn			=	alighn
        self.stats			=	stats
        self.state			=	CharState()
        self.gaem_class		=	gaem_class
        self.inventory		=	[]

    def addObject(self, _object: GameObject):
        self.inventory.append(_object)

    def delObject(self, id_: int):
        self.inventory.remove(id_ - 1)

    def delObjectAmmount(self, id_: int, ammount: int):
        self.inventory[id_ - 1].trow(1)

    def listObjects(self):
        return (((str(i) + ')) <' + self.inventory[i].name + '>::<' +
                  str(self.inventory[i].ammount) + '>\n')
                 for i in range(len(self.inventory))))

    def __str__(self):
        return ('<' + self.name + '>\n Class: ' + str(self.gaem_class.name))

    def damage(self, dmg_int: int = 1, true=False):
        if (true):
            self.state.HP -= dmg_int

class Gamer():
    '''Thing that plays and happens to be a discord user'''

    def __init__(self, user: discord.User, chars: dict = {}, rollingAs: Character = None,
                 isRolling: bool = False, isGM: bool = False):
        self.user			=	user
        self.chars			=	chars
        self.isRolling		=	isRolling
        self.rollingAs		=	rollingAs
        self.isGM 			=	isGM

    def __str__(self):
        return ('<' + str(self.user.name) + '>::<' + str(self.user.id) +
                '>\n' + ('This player is a GM\n' if (self.isGM) else '') +
                (('This player has the following Characters:' +
                  '\n'.join([x for x in self.chars])) if (self.chars) else
                 ('This player has no Characters')) +
                (('This player is rolling as: ' + self.rollingAs + '\n') if
                 (self.isRolling and bool(self.chars)) else ''))

class PlayerDB():

    def registerPlayer(self, player: Gamer):
        self.players.add(player)

    def removePlayer(self, player: Gamer):
        self.players.remove(player)

    def __init__(self):
        self.players = set()

    def __str__(self):
        return(str('Registered players are:' + ('\n\t'.join(str(gamer)) for gamer in self.players)))

class Campaing():
    '''A place where the game concurs, the state is kept'''

    def __init__(self, name: str, GM_: Gamer, description: str = "What title says",
                 notes: list = [], gamers: set = {}, Characters: list = []):
        self.name			=	name
        self.description	=	description
        self.notes			=	notes
        self.gamers			=	gamers
        self.GM				=	GM_

    def __str__(self):
        return (self.name + ':\n	'	+ self.description +
                '\n\tGame Master: ' + str(self.GM.user.mention) + '\n' + '\tPlayers: ' +
                '\n\t\t'.join([((str(gamer.user.mention))) for gamer in self.gamers]))

    def getNotes(self):
        return((str(index) + ':' + note) for note, index in enumerate(self.notes))

    def addNote(self, msg: str):
        self.notes.append(msg)

    def delNote(self, id_: int):
        self.notes.remove(id_)

class CampaingDB():

    def registerPlayer(self, campaing: Campaing):
        self.campaings.add(campaing)

    def removePlayer(self, campaing: Campaing):
        self.campaings.remove(campaing)

    def __str__(self):
        return(str('Registered campaings are:' +
               ('\n\t'.join(str(camp) for camp in self.campaings))))

    def __init__(self):
        self.campaings = set()

async def getPDB() -> PlayerDB:
    try:
        return(pickle.load(open(os.path.join(args.db, 'PDB.pkl'), 'rb')))
    except Exception as Err_:
        await logMe(Err_)
        return(PlayerDB())

async def getCDB() -> CampaingDB:
    try:
        return(pickle.load(open(os.path.join(args.db, 'CDB.pkl'), 'rb')))
    except Exception as Err_:
        await logMe(Err_)
        return(CampaingDB())

# init
bot = commands.Bot(command_prefix=config.CommandPrefix, case_insensitive=True)
os.makedirs(config.DB_PATH, exist_ok=True)

# All of this was carried over from Hijacked Node
async def logMe(st, err_=False, tq=True):
    if (err_):
        _stderr = '|-----------------ERR_ START-------------------|'
        print(_stderr) if (tq) else tqdm.write(_stderr)
        print(st) if (tq) else tqdm.write(st)
        try:
            with bot.get_channel(config.LogChan) as Chan:
                await Chan.send('|-----------------ERR_ START-------------------|')
                if (config.LogAdmin):
                    await Chan.send(
                        ' '.join([str(admin.mention) for admin in config.LogAdmin]))
                await Chan.send(st)
                await Chan.send('|------------------ERR_ END--------------------|')
        except:
            try:
                with bot.get_channel(config.debug) as Chan:
                    await Chan.send('|--------------- ERR_ START ----------------|')
                    try:
                        if (config.LogAdmin):
                            await Chan.send(
                                ' '.join([str(admin.mention) for admin in config.LogAdmin]))
                        await Chan.send(str(st))
                    except:
                        if (config.LogAdmin):
                            await Chan.send(
                                ' '.join([str(admin.mention)for admin in config.LogAdmin]))
                        await Chan.send("Some unprinteable error happened... ")
                    await Chan.send('|------------------ERR_ END--------------------|')
            except:
                _stderr = "Ah for hugs sake something went horribly grong! AGAIN"
                print(_stderr) if (tq) else tqdm.write(_stderr)
        _stderr = '|------------------ERR_ END--------------------|'
        print(_stderr) if (tq) else tqdm.write(_stderr)
    else:
        _stdout = st
        print(_stdout) if (tq) else tqdm.write(_stdout)
        try:
            with bot.get_channel(config.debug) as Chan:
                await Chan.send(st)
        except:
            try:
                with bot.get_channel(config.debug) as Chan:
                    try:
                        try:
                            await Chan.send(st)
                        except:
                            await Chan.send(str(type(st)))
                            await Chan.send(str(st))
                    except:
                        await Chan.send("Some unprinteable error happened... ")
            except:
                await Chan.send('|------------------Log_ START------------------|')
                await logMe("Ah for fucks sake something went horribly grong!", True)
                await Chan.send('|------------------Log_ END--------------------|')

@bot.event
async def on_command_error(context, exception):
    print('|--------------- ERR_ START ----------------|')
    print('Ignoring exception in command {}:'.format(context.command),
          file=sys.stderr)
    traceback.print_exception(type(exception),
                              exception,
                              exception.__traceback__,
                              file=sys.stderr)
    print('|---------------- ERR_ END -----------------|')
    try:
        await logMe(context.message.content)
    except:
        None
    try:
        await logMe(exception, True)
    except:
        None

@bot.event
async def on_error(event_method, *args, **kwargs):
    try:
        await logMe(" ``` " + event_method + " ``` ", True)
        await logMe(" ``` " + traceback.format_exc() + " ``` ", True)
    except:
        print('|------------------ERR_ START------------------|')
        print(' Ignoring exception in {}'.format(event_method), file=sys.stderr)
        traceback.print_exc()
        print('|------------------ ERR_ END ------------------|')

async def doBootUp():  # spagget
    await logMe('|-----------------doBootUp-st------------------|')
    # TODO: Think of a cool phrase to replace this one
    await logMe('|           Testing Testing 1, 2, 3            |')
    await logMe('|----------------------------------------------|')
    await bot.change_presence(activity=discord.Game(name='Waking Up...'))
    await logMe("[ " + str(dt.datetime.now().timestamp()) + " ]")
    await logMe(str(bot.user) + " Is connected to:")
    await logMe('|----------------------------------------------|')
    for guild in bot.guilds:
        await logMe(" - [" + str(guild.id) + "]: " + str(guild.name) + ".")
    global PDB
    global CDB
    PDB = await getPDB()
    CDB = await getCDB()
    await logMe('|----------------------------------------------|')
    await logMe("|           Bootup Sequence complete           |")
    await logMe('|----------------------------------------------|')
    await bot.change_presence(activity=discord.Game(name='Soulcasting'))
    await logMe('|----------------doBootUp End------------------|')

@bot.event
async def on_ready():
    await doBootUp()

# HERE BE DRAGONS;
# @bot.command(pass_context=True, brief='', description='')

@bot.group(pass_context=True, brief='Role System Command',
           description='Controls everything related roleplay mechanincs and meta')
async def role(ctx: discord.ext.commands.Context):
    if ctx.invoked_subcommand is None:
        await ctx.send('No valid subcommand was provied')

@role.group(pass_context=True, brief='Creates a new instance',
            description='Creates a new instance of the given object')
async def new(ctx: discord.ext.commands.Context):
    if ctx.invoked_subcommand is None:
        await ctx.send('No valid subpcommand was provided')

@new.group(pass_context=True)
async def character(ctx: discord.ext.commands.Context):
    if (ctx.author in PDB.get_players()):
        await ctx.send('')
    else:
        PDB.add_player(ctx.author)

# DRAGONS END HERE; #
bot.run(config.TOKEN)
