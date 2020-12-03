from hijackedrole.game.stats import StatsBase

from hijackedrole.game.classes import GameClass
from hijackedrole.game.stats.smart import CharStats
from hijackedrole.game.stats.dumb import DumbStats

from hijackedrole.game.stuff import InGameObject


class BaseCharacter():
    def __init__(self, name: str, alighn: list = [], stats: CharStats = None,
                 gclass: GameClass = None, dumb: bool = True):
        self.name			=	name
        self.alighn			=	alighn
        self.state			=	stats if (stats) else (DumbStats() if(dumb) else CharStats())
        self.gclass			=	gclass
        self.inventory		=	[]

    def addObject(self, _object: InGameObject) -> None:
        self.inventory.append(_object)

    def delObject(self, id_: int) -> None:
        self.inventory.remove(id_ - 1)

    def delObjectAmmount(self, id_: int, ammount: int) -> None:
        self.inventory[id_ - 1].trow(1)

    def listObjects(self) -> str:
        # TODO: THIS NEEDS TO BE REWORKED INTO A DICT
        return (
            ''.join([
                (f'[{str(i)}]<{self.inventory[i].name}>::<{str(self.inventory[i].ammount)}>\n')
                for i in range(len(self.inventory))
            ])
        )

    def __str__(self):
        return (f'<{self.name}>:\t- Class: {str(self.gclass.name)}')

    def damage(self, dmg_int: int = 1, true=False) -> None:  # TODO
        if (true):
            self.state.HP -= dmg_int

class PlayerCharacter(BaseCharacter):
    'TODO'
    def __init__(self, *args, **kargs):
        super.__init__(*args, **kargs)

class NonPlayerCharacter(BaseCharacter):
    'TODO'
    def __init__(self, *args, **kargs):
        super.__init__(*args, **kargs)

class VerySpecialCharacter(BaseCharacter):
    'TODO'
    ...
