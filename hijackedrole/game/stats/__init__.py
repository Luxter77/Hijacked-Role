from __future__ import annotations  # THANKS PYTHON DEVELOPERS YOU ARE GENUINELY GREAT
from statistics import median
from typing import Union
import numpy as np

class StatsBase():
    "Base operations for other stats"
    def averge(self) -> int:
        return(sum(list(self)) / len(self))

    def median(self) -> int:
        return median(list(self))

    def __bool__(self) -> bool:
        return(True)

    def __list__(self) -> list:
        "This one gets tricky, you have to do it by yourself!"
        return([])

    def __array__(self) -> np.array:
        return(np.array(list(self)))

    def __len__(self) -> int:
        return(len(list(self)))

    def __concat__(self) -> None:
        raise(NotImplementedError('No?????'))

    def __lt__(self, other) -> bool:
        return(self.averge() < other.averge())

    def __le__(self, other) -> bool:
        return((self.averge() < other.averge()) or (list(self) == list(other)))

    def __eq__(self, other) -> bool:
        return(list(self) == list(other))

    def __ge__(self, other) -> bool:
        return((list(self) == list(other)) or (self.averge() > other.averge()))

    def __gt__(self, other) -> bool:
        return(self.averge() > other.averge())

    def __mul__(self, other: Union[int, list]) -> StatsBase:
        try:
            if(len(self) == len(other)):
                return(self.__class__(asList=[(list(self)[i] * list(other)[i]) for i in range(0, len(self) - 1)]))
            else:
                return(self.__class__(asList=[(list(self)[i] * other) for i in range(0, len(self) - 1)]))
        except Exception:
            raise(NotImplementedError)

    def __truediv__(self, other: Union[int, list]) -> StatsBase:
        try:
            if(len(self) == len(other)):
                return(self.__class__(asList=[(list(self)[i] / list(other)[i]) for i in range(0, len(self) - 1)]))
            else:
                return(self.__class__(asList=[(list(self)[i] / other) for i in range(0, len(self) - 1)]))
        except Exception:
            raise(NotImplementedError)

    def __mod__(self, other: Union[int, list]) -> StatsBase:
        try:
            if(len(self) == len(other)):
                return(self.__class__(asList=[(list(self)[i] % list(other)[i]) for i in range(0, len(self) - 1)]))
            else:
                return(self.__class__(asList=[(list(self)[i] % other) for i in range(0, len(self) - 1)]))
        except Exception:
            raise(NotImplementedError)

    def __pow__(self, other: Union[int, list]) -> StatsBase:
        try:
            if(len(self) == len(other)):
                return(self.__class__(asList=[(list(self)[i] ** list(other)[i]) for i in range(0, len(self) - 1)]))
            else:
                return(self.__class__(asList=[(list(self)[i] ** other) for i in range(0, len(self) - 1)]))
        except Exception:
            raise(NotImplementedError)

    def __floordiv__(self, other: Union[int, list]) -> StatsBase:
        try:
            if(len(self) == len(other)):
                return(self.__class__(asList=[(list(self)[i] // list(other)[i]) for i in range(0, len(self) - 1)]))
            else:
                return(self.__class__(asList=[(list(self)[i] // other) for i in range(0, len(self) - 1)]))
        except Exception:
            raise(NotImplementedError)

    def __matmul__(self, other: Union[int, list]) -> StatsBase:
        try:
            if(len(self) == len(other)):
                return(self.__class__(asList=[(list(self)[i] @ list(other)[i]) for i in range(0, len(self) - 1)]))
            else:
                return(self.__class__(asList=[(list(self)[i] @ other) for i in range(0, len(self) - 1)]))
        except Exception:
            raise(NotImplementedError)

    def __xor__(self, other: Union[int, list]) -> StatsBase:
        try:
            if(len(self) == len(other)):
                return(self.__class__(asList=[(list(self)[i] ^ list(other)[i]) for i in range(0, len(self) - 1)]))
            else:
                return(self.__class__(asList=[(list(self)[i] ^ other) for i in range(0, len(self) - 1)]))
        except Exception:
            raise(NotImplementedError)
