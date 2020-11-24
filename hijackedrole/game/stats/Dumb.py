' These seem to be accurate, but maybe I readed the barrel wrong. '

from statistics import median 
import numpy as np
import random  # np.random is hugging slow

class DumbStats():
    '10:KILL.LEVEL.LOOT.GOTO 10'
    def averge(self) -> int:
        return int()

    def median(self) -> int:
        return median(list(self))

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
        
    def __list__(self):
        return([self.MaxHP, self.HP, self.MaxSP, self.SP, self.ATT, self.DEF, self.SPE, self.EAA, self.EDE, self.ACC, self.EVA])

    def __dic__(self) -> dict:
        return({'MaxHP': self.MaxHP, 'HP': self.HP, 'MaxSP': self.MaxSP,
                'SP': self.SP, 'ATT': self.ATT, 'DEF': self.DEF, 'SPE': self.SPE,
                'EAA': self.EAA, 'EDE': self.EDE, 'ACC': self.ACC, 'EVA': self.EVA})

    def __array__(self) -> np.array:
        return(np.array(list(self)))

    def __add__(self, other) -> 'DumbStats':
        if(len(self) == len(other)):
            return(DumbStats(asList=[(list(self)[i] + list(other)[i]) for i in range(0, len(self) - 1)]))
        elif(type(self) is int):
            return(DumbStats(asList=[(list(self)[i] + other) for i in range(0, len(self) - 1)]))
        else:
            raise(NotImplementedError)

    def __sub__(self, other) -> 'DumbStats':
        if(len(self) == len(other)):
            return(DumbStats(asList=[(list(self)[i] - list(other)[i]) for i in range(0, len(self) - 1)]))
        elif(type(self) is int):
            return(DumbStats(asList=[(list(self)[i] - other) for i in range(0, len(self) - 1)]))
        else:
            raise(NotImplementedError)
    
    def __mul__(self, other) -> 'DumbStats':
        if(len(self) == len(other)):
            return(DumbStats(asList=[(list(self)[i] * list(other)[i]) for i in range(0, len(self) - 1)]))
        elif(type(self) is int):
            return(DumbStats(asList=[(list(self)[i] * other) for i in range(0, len(self) - 1)]))
        else:
            raise(NotImplementedError)

    def __truediv__(self, other) -> 'DumbStats':
        if(len(self) == len(other)):
            return(DumbStats(asList=[(list(self)[i] / list(other)[i]) for i in range(0, len(self) - 1)]))
        elif(type(self) is int):
            return(DumbStats(asList=[(list(self)[i] / other) for i in range(0, len(self) - 1)]))
        else:
            raise(NotImplementedError)

    def __mod__(self, other) -> 'DumbStats':
        if(len(self) == len(other)):
            return(DumbStats(asList=[(list(self)[i] % list(other)[i]) for i in range(0, len(self) - 1)]))
        elif(type(self) is int):
            return(DumbStats(asList=[(list(self)[i] % other) for i in range(0, len(self) - 1)]))
        else:
            raise(NotImplementedError)

    def __pow__(self, other) -> 'DumbStats':
        if(len(self) == len(other)):
            return(DumbStats(asList=[(list(self)[i] ** list(other)[i]) for i in range(0, len(self) - 1)]))
        elif(type(self) is int):
            return(DumbStats(asList=[(list(self)[i] ** other) for i in range(0, len(self) - 1)]))
        else:
            raise(NotImplementedError)

    def __floordiv__(self, other) -> 'DumbStats':
        if(len(self) == len(other)):
            return(DumbStats(asList=[(list(self)[i] // list(other)[i]) for i in range(0, len(self) - 1)]))
        elif(type(self) is int):
            return(DumbStats(asList=[(list(self)[i] // other) for i in range(0, len(self) - 1)]))
        else:
            raise(NotImplementedError)

    def __matmul__(self, other) -> 'DumbStats':
        if(len(self) == len(other)):
            return(DumbStats(asList=[(list(self)[i] @ list(other)[i]) for i in range(0, len(self) - 1)]))
        elif(type(self) is int):
            return(DumbStats(asList=[(list(self)[i] @ other) for i in range(0, len(self) - 1)]))
        else:
            raise(NotImplementedError)

    def __xor__(self, other) -> 'DumbStats':
        if(len(self) == len(other)):
            return(DumbStats(asList=[(list(self)[i] ^ list(other)[i]) for i in range(0, len(self) - 1)]))
        elif(type(self) is int):
            return(DumbStats(asList=[(list(self)[i] ^ other) for i in range(0, len(self) - 1)]))
        else:
            raise(NotImplementedError)

    def __concat__(self) -> NotImplementedError:
        raise(NotImplementedError('No?????'))

    def __neg__(self) -> 'DumbStats':
        return(DumbStats(asList=[-x for x in self]))

    def __inv__(self) -> 'DumbStats':
        return(DumbStats(asList=[~x for x in self]))
    
    def __abs__(self) -> 'DumbStats':
        return(DumbStats(asList=[abs(x) for x in self]))

    def __len__(self) -> int:
        return(11)
    
    def __bool__(self) -> bool:
        return(True)

    def __str__(self) -> str:
        return(
            'MPP\t'	+	str(self.MaxHP)	+ '\tHOW MUCH CAN YOU BE PUNCHED BEFORE YOU DIE.' + 
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
            'EVA\t'	+	str(self.EVA)	+ '\tHOW FAST/WELL YOU REACT TO ENEMY MOVEMENTS.'
        )

    def __repr__(self) -> str:
        return(self.__str__())

    def __lt__(self, other) -> bool:
        return(self.averge() < other.averge())

    def __le__(self, other) -> bool:
        return((self.averge() < other.averge()) or (list(self) == list(other)))

    def __eq__(self, other) -> bool:
        return(list(self) == list(other))

    def __ne__(self, other) -> bool:
        return(list(self) != list(other))

    def __ge__(self, other) -> bool:
        return((list(self) == list(other)) or (self.averge() > other.averge()))

    def __gt__(self, other) -> bool:
        return(self.averge() > other.averge())
