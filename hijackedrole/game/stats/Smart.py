' Double barrel disruptor shoot spreading DEMOCRACY -> RIP Maru 2020'

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
    def averge(self) -> int:
        return int()

    def median(self) -> int:
        return median(list(self))

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

    def __array__(self) -> np.array:
        return(np.array(list(self)))

    def __mul__(self, other) -> 'CharStats':
        if(len(self) == len(other)):
            return(CharStats(asList=[(list(self)[i] * list(other)[i]) for i in range(0, len(self) - 1)]))
        elif(type(self) is int):
            return(CharStats(asList=[(list(self)[i] * other) for i in range(0, len(self) - 1)]))
        else:
            raise(NotImplementedError)

    def __truediv__(self, other) -> 'CharStats':
        if(len(self) == len(other)):
            return(CharStats(asList=[(list(self)[i] / list(other)[i]) for i in range(0, len(self) - 1)]))
        elif(type(self) is int):
            return(CharStats(asList=[(list(self)[i] / other) for i in range(0, len(self) - 1)]))
        else:
            raise(NotImplementedError)

    def __mod__(self, other) -> 'CharStats':
        if(len(self) == len(other)):
            return(CharStats(asList=[(list(self)[i] % list(other)[i]) for i in range(0, len(self) - 1)]))
        elif(type(self) is int):
            return(CharStats(asList=[(list(self)[i] % other) for i in range(0, len(self) - 1)]))
        else:
            raise(NotImplementedError)

    def __pow__(self, other) -> 'CharStats':
        if(len(self) == len(other)):
            return(CharStats(asList=[(list(self)[i] ** list(other)[i]) for i in range(0, len(self) - 1)]))
        elif(type(self) is int):
            return(CharStats(asList=[(list(self)[i] ** other) for i in range(0, len(self) - 1)]))
        else:
            raise(NotImplementedError)

    def __floordiv__(self, other) -> 'CharStats':
        if(len(self) == len(other)):
            return(CharStats(asList=[(list(self)[i] // list(other)[i]) for i in range(0, len(self) - 1)]))
        elif(type(self) is int):
            return(CharStats(asList=[(list(self)[i] // other) for i in range(0, len(self) - 1)]))
        else:
            raise(NotImplementedError)

    def __matmul__(self, other) -> 'CharStats':
        if(len(self) == len(other)):
            return(CharStats(asList=[(list(self)[i] @ list(other)[i]) for i in range(0, len(self) - 1)]))
        elif(type(self) is int):
            return(CharStats(asList=[(list(self)[i] @ other) for i in range(0, len(self) - 1)]))
        else:
            raise(NotImplementedError)

    def __xor__(self, other) -> 'CharStats':
        if(len(self) == len(other)):
            return(CharStats(asList=[(list(self)[i] ^ list(other)[i]) for i in range(0, len(self) - 1)]))
        elif(type(self) is int):
            return(CharStats(asList=[(list(self)[i] ^ other) for i in range(0, len(self) - 1)]))
        else:
            raise(NotImplementedError)

    def __concat__(self) -> NotImplementedError:
        raise(NotImplementedError('No?????'))

    def __neg__(self) -> 'CharStats':
        return(CharStats(asList=[-x for x in self]))

    def __inv__(self) -> 'CharStats':
        return(CharStats(asList=[~x for x in self]))
    
    def __abs__(self) -> 'CharStats':
        return(CharStats(asList=[abs(x) for x in self]))

    def __len__(self) -> int:
        return(10)
    
    def __bool__(self) -> bool:
        return(True)

    def __list__(self) -> list:
        return([self.strg, self.inte, self.sped, self.dext, self.wisd,
                self.conn, self.char, self.luck, self.levl, self.seed])

    def __dic__(self) -> dict:
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
