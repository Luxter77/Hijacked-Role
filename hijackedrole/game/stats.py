' These seem to be accurate, but maybe I readed the barrel wrong. '

from statistics import median 
import numpy as np
import random  # np.random is hugging slow


class CharStats():
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
            self.strg, self.inte, self.sped, self.dext, self.wisd = asList[:5]  # the things I do so
            self.conn, self.char, self.luck, self.levl, self.seed = asList[5:]  # flake8 is happy :)
        else:
            self.strg, self.inte, self.sped, self.dext, self.wisd = strg, inte, sped, dext, wisd
            self.conn, self.char, self.luck, self.levl, self.seed = conn, char, luck, levl, seed
            self.seed = seed if (seed) else random.randint(-65535, 65536)

    def __list__(self) -> list:
        return([self.strg, self.inte, self.sped, self.dext, self.wisd,
                self.conn, self.char, self.luck, self.levl, self.seed])

    def __array__(self) -> np.array:
        return(np.array(self.__list__))

    def __add__(self, other) -> 'CharStats':
        return(CharStats(asList=[self.strg + other.strg, self.inte + other.inte,
                                 self.sped + other.sped, self.dext + other.dext,
                                 self.wisd + other.wisd, self.conn + other.conn,
                                 self.char + other.char, self.luck + other.luck,
                                 self.levl + other.levl, max((self.seed + other.seed) / 2, -65536)]))

    def __sub__(self, other) -> 'CharStats':
        return(CharStats(asList=[self.strg - other.strg, self.inte - other.inte,
                                 self.sped - other.sped, self.dext - other.dext,
                                 self.wisd - other.wisd, self.conn - other.conn,
                                 self.char - other.char, self.luck - other.luck,
                                 self.levl - other.levl, min((self.seed - other.seed) * 2, 65536)]))

    def __dict__(self) -> dict:
        return({'strg': self.strg, 'inte': self.inte, 'sped': self.sped, 'dext': self.dext,
                'wisd': self.wisd, 'conn': self.conn, 'char': self.char, 'luck': self.luck,
                'levl': self.levl, 'seed': self.seed})

    def __str__(self) -> str:
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
            '\n\tmagic number:\t' +	str(self.seed) + 	' How.'
        )

    def __repr__(self) -> str:
        return(self.__str__())


class DumbStats():
    '10:KILL.LEVEL.LOOT.GOTO 10'
    def averge(self) -> int:
        return int((self.ATT + self.DEF + self.SPE + self.EAA + self.EDE + self.ACC + self.EVA) / 7)

    def median(self) -> int:
        return median(list(self))

    def __init__(self, initMaxHP: int = 5, initMaxSP: int = 5,
                 ATT: int = None, DEF: int = None, SPE: int = None,
                 EAA: int = None, EDE: int = None, ACC: int = None,
                 EVA: int = None, asList: list = None):
        self.MaxHP = self.HP = initMaxHP
        self.MaxSP = self.SP = initMaxSP
        if(asList):
            self.ATT = ATT if(ATT) else random.randint(5, 10)
            self.DEF = DEF if(DEF) else random.randint(5, 10)
            self.SPE = SPE if(SPE) else random.randint(5, 10)
            self.EAA = EAA if(EAA) else random.randint(5, 10)
            self.EDE = EDE if(EDE) else random.randint(5, 10)
            self.ACC = ACC if(ACC) else random.randint(5, 10)
            self.EVA = EVA if(EVA) else random.randint(5, 10)
        else:
            self.ATT, self.DEF, self.SPE, self.EAA, self.EDE, self.ACC, self.EVA = asList

    def __iter__(self):
        return(x for x in list(self))

    def __floordiv__(self, other) -> 'DumbStats':
        return(DumbStats(asList=[(list(self)[i] // list(other)[i]) for i in range(0, len(self) - 1)]))

    def __dic__(self) -> dict:
        return({'ATT': self.ATT, 'DEF': self.DEF, 'SPE': self.SPE, 'EAA': self.EAA,
                'EDE': self.EDE, 'ACC': self.ACC, 'EVA': self.EVA})

    def __array__(self) -> np.array:
        return(np.array([self.ATT, self.DEF, self.SPE, self.EAA, self.EDE, self.ACC, self.EVA]))

    def __add__(self, other) -> 'DumbStats':
        return(DumbStats(asList=[self.ATT + other.ATT, self.DEF + other.DEF,
                                 self.SPE + other.SPE, self.EAA + other.EAA,
                                 self.EDE + other.EDE, self.ACC + other.ACC,
                                 self.EVA + other.EVA]))

    def __sub__(self, other) -> 'DumbStats':
        return(DumbStats(asList=[self.ATT - other.ATT, self.DEF - other.DEF,
                                 self.SPE - other.SPE, self.EAA - other.EAA,
                                 self.EDE - other.EDE, self.ACC - other.ACC,
                                 self.EVA - other.EVA]))

    def __mod__(self, other) -> 'DumbStats':
        return(DumbStats(asList=[(list(self)[i] % list(other)[i]) for i in range(0, len(self) - 1)]))
    
    def __mul__(self, other) -> 'DumbStats':
        return(DumbStats(asList=[(list(self)[i] * list(other)[i]) for i in range(0, len(self) - 1)]))

    def __mul__(self, other) -> 'DumbStats':
        return(DumbStats(asList=[(list(self)[i] @ list(other)[i]) for i in range(0, len(self) - 1)]))

    def __pow__(self, other) -> 'DumbStats':
        return(DumbStats(asList=[(list(self)[i] ** list(other)[i]) for i in range(0, len(self) - 1)]))

    def __truediv__(self, other) -> 'DumbStats':
        return(DumbStats(asList=[(list(self)[i] / list(other)[i]) for i in range(0, len(self) - 1)]))

    def __xor__(self, other) -> 'DumbStats':
        return(DumbStats(asList=[(list(self)[i] ^ list(other)[i]) for i in range(0, len(self) - 1)]))

    def __concat__(self) -> NotImplementedError:
        raise(NotImplementedError('No?????'))

    def __neg__(self) -> 'DumbStats':
        return(DumbStats(asList=[-x for x in self]))

    def __inv__(self) -> 'DumbStats':
        return(DumbStats(asList=[~x for x in self]))
    
    def __abs__(self) -> 'DumbStats':
        return(DumbStats(asList=[abs(x) for x in self]))

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
