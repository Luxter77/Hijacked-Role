import random

from discord import User as DiscordUser

from hijackedrole.game.characters import PlayerCharacter

class Gamer():
    '''Thing that plays and happens to be a discord user'''

    def __init__(self, user: DiscordUser, chars: dict = {}, rollingAs: PlayerCharacter = None,
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
