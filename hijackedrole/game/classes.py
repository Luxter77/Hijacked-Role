''' This file is just filled with pain. '''


class GameClass():
    'TODO: change classes to somethign more original'
    'TODO: Make it so there are other classes'
    'for now, just DnD classes'
    def __init__(self, name: str, dice: list, clvl: int = 1, rng: bool = True):
        self.dice = dice
        self.name = name
        self.clvl = clvl
        self.rng = rng

    def __str__(self):
        return ('<' + self.name + '>::<lvl:' + str(self.clvl) + '>')


# Implementation of Margaret Hartwell's and Joshua Chen's archeotype thingy
# TODO: ACTUALLY FINISH THIS
# It was a pain to do


class CaregiverFamily(GameClass):
    ...


class Caregiver(CaregiverFamily):
    ...


class Angel(CaregiverFamily):
    ...


class Guardian(CaregiverFamily):
    ...


class Healer(CaregiverFamily):
    ...


class Samaritan(CaregiverFamily):
    ...


class CitizenFamily(GameClass):
    ...


class Citizen(CitizenFamily):
    ...


class Advocate(CitizenFamily):
    ...


class Everyman(CitizenFamily):
    ...


class Networker(CitizenFamily):
    ...


class Servant(CitizenFamily):
    ...


class CreatorFamily(GameClass):
    ...


class Creator(CreatorFamily):
    ...


class Artist(CreatorFamily):
    ...


class Entrepreneur(CreatorFamily):
    ...


class Storyteller(CreatorFamily):
    ...


class Visionary(CreatorFamily):
    ...


class ExplorerFamily(GameClass):
    ...


class Explorer(ExplorerFamily):
    ...


class Adventurer(ExplorerFamily):
    ...


class Pioneer(ExplorerFamily):
    ...


class Generalist(ExplorerFamily):
    ...


class Seeker(ExplorerFamily):
    ...


class HeroFamily(GameClass):
    ...


class Hero(HeroFamily):
    ...


class Athlete(HeroFamily):
    ...


class Liberator(HeroFamily):
    ...


class Rescuer(HeroFamily):
    ...


class Warrior(HeroFamily):
    ...


class InnocentFamily(GameClass):
    ...


class Innocent(InnocentFamily):
    ...


class Child(InnocentFamily):
    ...


class Dreamer(InnocentFamily):
    ...


class Idealist(InnocentFamily):
    ...


class Muse(InnocentFamily):
    ...


class JesterFamily(GameClass):
    ...


class Jester(JesterFamily):
    ...


class Clown(JesterFamily):
    ...


class Entertainer(JesterFamily):
    ...


class Provocateur(JesterFamily):
    ...


class Shapeshifter(JesterFamily):
    ...


class LoverFamily(GameClass):
    ...


class Lover(LoverFamily):
    ...


class Companion(LoverFamily):
    ...


class Hedonist(LoverFamily):
    ...


class Matchmaker(LoverFamily):
    ...


class Romantic(LoverFamily):
    ...


class MagicianFamily(GameClass):
    ...


class Magician(MagicianFamily):
    ...


class Alchemist(MagicianFamily):
    ...


class Engineer(MagicianFamily):
    ...


class Innovator(MagicianFamily):
    ...


class Scientist(MagicianFamily):
    ...


class RebelFamily(GameClass):
    ...


class Rebel(RebelFamily):
    ...


class Activist(RebelFamily):
    ...


class Gambler(RebelFamily):
    ...


class Maverick(RebelFamily):
    ...


class Reformer(RebelFamily):
    ...


class SageFamily(GameClass):
    ...


class Sage(SageFamily):
    ...


class Detective(SageFamily):
    ...


class Mentor(SageFamily):
    ...


class Shaman(SageFamily):
    ...


class Translator(SageFamily):
    ...


class SovereignFamily(GameClass):
    ...


class Sovereign(SovereignFamily):
    ...


class Ambassador(SovereignFamily):
    ...


class Judge(SovereignFamily):
    ...


class Patriarch(SovereignFamily):
    ...


class Ruler(SovereignFamily):
    ...


# TOTALLY NOT LIZZARDS AND OUBLIETTES
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
