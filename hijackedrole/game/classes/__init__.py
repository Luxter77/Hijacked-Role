# TODO: ACTUALLY FINISH THIS
# It was a pain to do

from typing import List

from random import randint


class Dice():
    def __init__(self, n: int, a: int = 1):
        """'n': 'faces',\n 'a': 'ammount of dice'"""
        if(n < -0): raise(ValueError(f"'n' must be non-negative!\n a was: {str(n)}"))
        if(a < -0): raise(ValueError(f"'a' must be non-negative!\n a was: {str(a)}"))
        self.n, self.a = n, a

    def rollWithAdventage(self) -> dict:
        'Roll Two times and pick the greater resoult'
        self.resoults = [max(randint(1, self.n), randint(1, self.n)) for _ in range(self.a)]
        self.resoult  = sum(self.resoults)
        return({'resoults': self.resoults, 'resoult': self.resoult})

    def rollWithDisAdventage(self) -> dict:
        'Roll Two times and pick the smaller resoult'
        self.resoults = [min(randint(1, self.n), randint(1, self.n)) for _ in range(self.a)]
        self.resoult  = sum(self.resoults)
        return({'resoults': self.resoults, 'resoult': self.resoult})

    def roll(self) -> dict:
        'Roll the dise'
        self.resoults = [randint(1, self.n) for _ in range(self.a)]
        self.resoult  = sum(self.resoults)
        return({'resoults': self.resoults, 'resoult': self.resoult})

CDice = List[Dice]

class GameClass():
    'TODO: change classes to somethign more original'
    'TODO: Make it so there are other classes'

    def __init__(self, cname: str, cdice: CDice, clvl: int = 1, rng: bool = True):
        self.cdice = cdice
        self.cname = cname
        self.clvl = clvl
        self.rng = rng

    def __str__(self) -> str:
        if(self.clvl > 1):
            return(f'\t<{self.cname}>::<lvl:{str(self.clvl)}>::<{self.cdice[1].a}D{self.cdice[0].n}>')
        else:
            return(f'\t<{self.cname}>::<lvl:{str(self.clvl)}>::<{self.cdice[1].a}D{self.cdice[1].n}>')

    def __eq__(self, other) -> bool:
        return(list(self) == list(other))
