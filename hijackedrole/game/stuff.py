import random

from discord.channel import TextChannel
from discord import User

from hijackedrole.game.classes import GameClass

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

    def trow(self, ammount: int = 1) -> None:
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

    def addObject(self, _object: GameObject) -> None:
        self.inventory.append(_object)

    def delObject(self, id_: int) -> None:
        self.inventory.remove(id_ - 1)

    def delObjectAmmount(self, id_: int, ammount: int) -> None:
        self.inventory[id_ - 1].trow(1)

    def listObjects(self) -> str:
        # TODO: THIS NEEDS TO BE REWORKED INTO A DICT
        return (((str(i) + ')) <' + self.inventory[i].name + '>::<' +
                  str(self.inventory[i].ammount) + '>\n')
                 for i in range(len(self.inventory))))

    def __str__(self):
        return ('<' + self.name + '>\n Class: ' + str(self.gaem_class.name))

    def damage(self, dmg_int: int = 1, true=False) -> None:
        if (true):
            self.state.HP -= dmg_int

class Gamer():
    '''Thing that plays and happens to be a discord user'''

    def __init__(self, user: User, chars: dict = {}, rollingAs: Character = None,
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
    # TODO: REWORK INTO A POSGRESQL DATABASE OR SOMETHING
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
    # TODO: REWORK INTO A POSGRESQL DATABASE OR SOMETHING
    def registerPlayer(self, campaing: Campaing):
        self.campaings.add(campaing)

    def removePlayer(self, campaing: Campaing):
        self.campaings.remove(campaing)

    def __str__(self):
        return(str('Registered campaings are:' +
               ('\n\t'.join(str(camp) for camp in self.campaings))))

    def __init__(self):
        self.campaings = set()
