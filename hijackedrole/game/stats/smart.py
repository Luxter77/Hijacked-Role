' Double barrel disruptor shoot spreading DEMOCRACY -> RIP Maru 2020'
from __future__ import annotations
import random

from hijackedrole.game.stats import StatsBase

class CharStats(StatsBase):
    '''
    strength        (strg): How much you strong,\n
    inteligence     (inte): How much you think,\n
    speed           (sped): How fast you move,\n
    dexterity       (dext): How well you move,\n
    wisdom          (wisd): How well you think,\n
    constitution	(conn): How well you,\n
    carisma         (char): How nice you,\n
    luck            (luck): How well you,\n
    level           (levl): How much have you,\n
    seed            (seed): How.
    '''
    def __init__(self, strg: int = 10, inte: int = 10, sped: int = 10, dext: int = 10,
                 wisd: int = 10, conn: int = 10, char: int = 10, luck: int = 50,
                 levl: int = 1, seed: int = None, asList: list = None) -> None:
        if(asList):
            if(len(asList) != len(self)):
                raise(IndexError(f'asList must have exactly {str(len(self))} entries'))
            self.strg, self.inte, self.sped, self.dext, self.wisd = asList[:5]  # the things I do so
            self.conn, self.char, self.luck, self.levl, self.seed = asList[5:]  # flake8 is happy :)
        else:
            self.strg, self.inte, self.sped, self.dext, self.wisd = strg, inte, sped, dext, wisd
            self.conn, self.char, self.luck, self.levl, self.seed = conn, char, luck, levl, seed
            self.seed = seed if (seed) else random.randint(-65535, 65536)
        super.__init__()

    def __list__(self) -> list:
        return([self.strg, self.inte, self.sped, self.dext, self.wisd,
                self.conn, self.char, self.luck, self.levl, self.seed])

    def __dic__(self) -> dict:
        return({'strg': self.strg, 'inte': self.inte, 'sped': self.sped,
                'dext': self.dext, 'wisd': self.wisd, 'conn': self.conn,
                'char': self.char, 'luck': self.luck, 'levl': self.levl,
                'seed': self.seed})

    def __add__(self, other: CharStats) -> CharStats:
        return(CharStats(asList=[self.strg + other.strg, self.inte + other.inte,
                                 self.sped + other.sped, self.dext + other.dext,
                                 self.wisd + other.wisd, self.conn + other.conn,
                                 self.char + other.char, self.luck + other.luck,
                                 self.levl + other.levl,
                                 max((self.seed + other.seed) / 2, -65536)]))

    def __sub__(self, other: CharStats) -> CharStats:
        return(CharStats(asList=[self.strg - other.strg, self.inte - other.inte,
                                 self.sped - other.sped, self.dext - other.dext,
                                 self.wisd - other.wisd, self.conn - other.conn,
                                 self.char - other.char, self.luck - other.luck,
                                 self.levl - other.levl,
                                 min((self.seed - other.seed) * 2, 65536)]))

    def __neg__(self) -> CharStats:
        return(CharStats(asList=[-self.strg, -self.inte, -self.sped, -self.dext, -self.wisd,
                                 -self.conn, -self.char, -self.luck, -self.levl, -self.seed]))

    def __inv__(self) -> CharStats:
        return(CharStats(asList=[~self.strg, ~self.inte, ~self.sped, ~self.dext, ~self.wisd,
                                 ~self.conn, ~self.char, ~self.luck, ~self.levl, ~self.seed]))

    def __abs__(self) -> CharStats:
        return(CharStats(asList=[abs(self.strg), abs(self.inte), abs(self.sped),
                                 abs(self.dext), abs(self.wisd), abs(self.conn),
                                 abs(self.char), abs(self.luck), abs(self.levl),
                                 abs(self.seed)]))

    def __len__(self) -> int:
        return(10)

    def __str__(self) -> str:
        return (
            f'\n\tstr:\t\t\t{str(self.strg)}\tHow much you strong' +
            f'\n\tint:\t\t\t{str(self.inte)}\tHow much you think' +
            f'\n\tspd:\t\t\t{str(self.sped)}\tHow fast you move' +
            f'\n\tdex:\t\t\t{str(self.dext)}\tHow well you move' +
            f'\n\twis:\t\t\t{str(self.wisd)}\tHow well you think' +
            f'\n\tcon:\t\t\t{str(self.conn)}\tHow well you' +
            f'\n\tchr:\t\t\t{str(self.char)}\tHow you' +
            f'\n\tluk:\t\t\t{str(self.luck)}\tHow well' +
            f'\n\tlvl:\t\t\t{str(self.levl)}\tHow much' +
            f'\n\tMN°:\t\t\t{str(self.seed)}\tHow.'
        )
