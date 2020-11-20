class GameClass():
    "TODO: change classes to somethign more original"
    "TODO: Make it so there are other classes"
    "for now, just DnD classes"
    def __init__(self, name: str, dice: list, clvl: int = 1, rng: bool = True):
        self.dice = dice
        self.name = name
        self.clvl = clvl
        self.rng = rng

    def __str__(self):
        return ('<' + self.name + '>::<lvl:' + str(self.clvl) + '>')

class Barbarian(GameClass):
    name = 'barbarian'
    dice = [[1, 12], [7, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)

class Bard(GameClass):
    name = 'bard'
    dice = [[1, 8], [5, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)

class Cleric(GameClass):
    name = 'cleric'
    dice = [[1, 8], [5, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)
class Druid(GameClass):
    name = 'druid'
    dice = [[1, 8], [5, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)
class Fighter(GameClass):
    name = 'fighter'
    dice = [[1, 10], [6, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)

class Monk(GameClass):
    name = 'monk'
    dice = [[1, 8], [5, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)

class Paladin(GameClass):
    name = 'paladin'
    dice = [[1, 10], [6, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)

class Ranger(GameClass):
    name = 'ranger'
    dice = [[1, 10], [6, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)

class Rogue(GameClass):
    name = 'rogue'
    dice = [[1, 8], [5, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)

class Sorcerer(GameClass):
    name = 'sorcerer'
    dice = [[1, 6], [4, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)

class Warlock(GameClass):
    name = 'warlock'
    dice = [[1, 8], [5, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)

class Wizard(GameClass):
    name = 'wizard'
    dice = [[1, 6], [4, 1]]

    def __init__(self, rng: bool = True):
        super().__init__(name=self.name, dice=self.dice, rng=rng)
