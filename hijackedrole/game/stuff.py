from typing import Union

from hijackedrole.game.stats import StatsBase

from hijackedrole.game.stats.smart import CharStats
from hijackedrole.game.stats.dumb import DumbStats

class InGameObject():
    '''TODO: MOVE TO OWN MODULI'''
    '''A thing that a Character can have or equip or use'''
    def __init__(self, name: str, stats: Union[DumbStats, CharStats], description: str = "What title says",
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
