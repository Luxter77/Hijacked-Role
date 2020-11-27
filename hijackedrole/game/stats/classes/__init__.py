# Implementation of Margaret Hartwell's and Joshua Chen's archeotype thingy
# TODO: ACTUALLY FINISH THIS
# It was a pain to do

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

    def __eq__(self, other):
        return(list(self) == list(other))
    
