from hijackedrole.game.classes import GameClass, Dice, CDice

class Barbarian(GameClass):
    def __init__(self, cname: str = 'Barbarian',
                 cdice: CDice = [Dice(1, 12), Dice(7, 1)],
                 rng: bool = True):
        super().__init__(
            cname=cname,
            cdice=cdice,
            rng=rng
        )

class Bard(GameClass):
    def __init__(self, cname: str = 'Bard',
                 cdice: CDice = [Dice(1, 8), Dice(5, 1)],
                 rng: bool = True):
        super().__init__(
            cname=cname,
            cdice=cdice,
            rng=rng
        )

class Cleric(GameClass):
    def __init__(self, cname: str = 'Cleric',
                 cdice: CDice = [Dice(1, 8), Dice(5, 1)],
                 rng: bool = True):
        super().__init__(
            cname=cname,
            cdice=cdice,
            rng=rng
        )

class Druid(Cleric):
    def __init__(self, cname: str = 'Druid',
                 cdice: CDice = [Dice(1, 8), Dice(5, 1)],
                 rng: bool = True):
        super().__init__(
            cname=cname,
            cdice=cdice,
            rng=rng
        )

class Fighter(GameClass):
    def __init__(self, cname: str = 'Fighter',
                 cdice: CDice = [Dice(1, 10), Dice(6, 1)],
                 rng: bool = True):
        super().__init__(
            cname=cname,
            cdice=cdice,
            rng=rng
        )

class Monk(GameClass):
    def __init__(self, cname: str = 'Monk',
                 cdice: CDice = [Dice(1, 8), Dice(5, 1)],
                 rng: bool = True):
        super().__init__(
            cname=cname,
            cdice=cdice,
            rng=rng
        )

class Paladin(GameClass):
    def __init__(self, cname: str = 'Paladin',
                 cdice: CDice = [Dice(1, 10), Dice(6, 1)],
                 rng: bool = True):
        super().__init__(
            cname=cname,
            cdice=cdice,
            rng=rng
        )

class Ranger(GameClass):
    def __init__(self, cname: str = 'Ranger',
                 cdice: CDice = [Dice(1, 10), Dice(6, 1)],
                 rng: bool = True):
        super().__init__(
            cname=cname,
            cdice=cdice,
            rng=rng
        )

class Rogue(GameClass):
    def __init__(self, cname: str = 'Rogue',
                 cdice: CDice = [Dice(1, 8), Dice(5, 1)],
                 rng: bool = True):
        super().__init__(
            cname=cname,
            cdice=cdice,
            rng=rng
        )

class Sorcerer(GameClass):
    def __init__(self, cname: str = 'Sorcerer',
                 cdice: CDice = [Dice(1, 6), Dice(4, 1)],
                 rng: bool = True):
        super().__init__(
            cname=cname,
            cdice=cdice,
            rng=rng
        )

class Warlock(GameClass):
    def __init__(self, cname: str = 'Warlock',
                 cdice: CDice = [Dice(1, 8), Dice(5, 1)],
                 rng: bool = True):
        super().__init__(
            cname=cname,
            cdice=cdice,
            rng=rng
        )

class Wizard(GameClass):
    def __init__(self, cname: str = 'Wizard',
                 cdice: CDice = [Dice(1, 6), Dice(4, 1)],
                 rng: bool = True):
        super().__init__(
            cname=cname,
            cdice=cdice,
            rng=rng
        )
