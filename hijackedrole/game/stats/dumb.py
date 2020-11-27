' These seem to be accurate, but maybe I readed the barrel wrong. '
from __future__ import annotations
import random

from hijackedrole.game.stats.base import StatsBase

class DumbStats():
    '10:KILL.LEVEL.LOOT.GOTO 10'
    def __init__(self, initMaxHP: int = 5, initMaxSP: int = 5,
                 ATT: int = None, DEF: int = None, SPE: int = None,
                 EAA: int = None, EDE: int = None, ACC: int = None,
                 EVA: int = None, asList: list = None):
        if(asList):
            if(len(asList) != len(self)):
                raise(IndexError(f'asList must have exactly {str(len(self))} entries'))
            self.MaxHP, self.HP, self.MaxSP, self.SP, self.ATT, self.DEF, self.SPE, self.EAA, self.EDE, self.ACC, self.EVA = asList
        else:
            self.MaxHP = self.HP = initMaxHP
            self.MaxSP = self.SP = initMaxSP
            self.ATT = ATT if(ATT) else random.randint(5, 10)
            self.DEF = DEF if(DEF) else random.randint(5, 10)
            self.SPE = SPE if(SPE) else random.randint(5, 10)
            self.EAA = EAA if(EAA) else random.randint(5, 10)
            self.EDE = EDE if(EDE) else random.randint(5, 10)
            self.ACC = ACC if(ACC) else random.randint(5, 10)
            self.EVA = EVA if(EVA) else random.randint(5, 10)
        super.__init__()

    def __list__(self):
        return([self.MaxHP, self.HP, self.MaxSP, self.SP, self.ATT,
                self.DEF, self.SPE, self.EAA, self.EDE, self.ACC, self.EVA])

    def __dic__(self) -> dict:
        return({'MaxHP': self.MaxHP, 'HP': self.HP, 'MaxSP': self.MaxSP,
                'SP': self.SP, 'ATT': self.ATT, 'DEF': self.DEF, 'SPE': self.SPE,
                'EAA': self.EAA, 'EDE': self.EDE, 'ACC': self.ACC, 'EVA': self.EVA})

    def __add__(self, other: DumbStats) -> DumbStats:
        return(DumbStats(asList=[self.MaxHP + other.MaxHP, self.MaxSP + other.MaxSP,
                                 self.ATT + other.ATT, self.DEF + other.DEF,
                                 self.SPE + other.SPE, self.EAA + other.EAA,
                                 self.EDE + other.EDE, self.ACC + other.ACC,
                                 self.EVA + other.EVA]))

    def __sub__(self, other: DumbStats) -> DumbStats:
        return(DumbStats(asList=[self.MaxHP - other.MaxHP, self.MaxSP - other.MaxSP,
                                 self.ATT - other.ATT, self.DEF - other.DEF,
                                 self.SPE - other.SPE, self.EAA - other.EAA,
                                 self.EDE - other.EDE, self.ACC - other.ACC,
                                 self.EVA - other.EVA]))

    def __neg__(self) -> DumbStats:
        return(DumbStats(asList=[-self.MaxHP, -self.HP, -self.MaxSP,
                                 -self.SP, -self.ATT, -self.DEF,
                                 -self.SPE, -self.EAA, -self.EDE,
                                 -self.ACC, -self.EVA]))

    def __inv__(self) -> DumbStats:
        return(DumbStats(asList=[~self.MaxHP, ~self.HP, ~self.MaxSP,
                                 ~self.SP, ~self.ATT, ~self.DEF,
                                 ~self.SPE, ~self.EAA, ~self.EDE,
                                 ~self.ACC, ~self.EVA]))

    def __abs__(self) -> DumbStats:
        return(DumbStats(asList=[abs(self.MaxHP), abs(self.HP), abs(self.MaxSP),
                                 abs(self.SP), abs(self.ATT), abs(self.DEF),
                                 abs(self.SPE), abs(self.EAA), abs(self.EDE),
                                 abs(self.ACC), abs(self.EVA)]))

    def __len__(self) -> int:
        return(11)

    def __str__(self) -> str:
        return('MPP\t'	+	str(self.MaxHP)	+ '\tHOW MUCH CAN YOU BE PUNCHED BEFORE YOU DIE.' +
               ''      +   ''                 + '(IN GENERAL)\n' +
               'HPP\t'	+	str(self.HP)	+ '\tHOW MUCH CAN YOU BE PUNCHED BEFORE YOU DIE.' +
               ''      +   ''                 + '(NOW)\n' +
               'MAP\t'	+	str(self.MaxHP)	+ '\tHOW MUCH CAN YOU PUNCH BEFORE YOU CAN\'T.' +
               ''      +   ''                 + '(IN GENERAL)\n' +
               'SPP\t'	+	str(self.HP)	+ '\tHOW MUCH CAN YOU PUNCH BEFORE YOU CAN\'T.' +
               ''      +   ''                 + '(NOW)\n\n' +
               'ATT\t'	+	str(self.ATT)	+ '\tHOW STRONG YOU ATTACK OTHER PEOPLE.\n' +
               'DEF\t'	+	str(self.DEF)	+ '\tHOW MUCH YOU DEFEND WHEN ATTACKED.\n' +
               'SPE\t'	+	str(self.SPE)	+ '\tHOW FAST YOU MOVE; WHAT DID YOU EXPECT?\n' +
               'EAA\t'	+	str(self.EAA)	+ '\tHOW WELL YOU ATTACK OTHER PEOPLE.\n''' +
               'EDE\t'	+	str(self.EDE)	+ '\tHOW WELL YOU DEFFEND FROM OTHER PEOPLE.\n' +
               'ACC\t'	+	str(self.ACC)	+ '\tHOW WELL YOU TRACK ENEMY MOVEMENTS.\n' +
               'EVA\t'	+	str(self.EVA)	+ '\tHOW FAST/WELL YOU REACT TO ENEMY MOVEMENTS.')
