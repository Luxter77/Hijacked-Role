#!/usr/bin/env python3
# coding: utf-8
class game_class():
	"TODO: Make it so there are other classes"
	"for now, just DnD classes"
	def __init__(self, name: str, dice: list, clvl: int = 1, rng: bool = True):
		self.dice			= dice
		self.name			= name
		self.clvl			= clvl
		self.rng			= rng
	def __str__(self):
		return('<' + self.name + '>::<lvl:' + str(self.clvl) + '>')

class BARBARIAN(game_class):
	name 		= 'barbarian'
	dice		= [[1, 12], [7, 1]]
	def __init__(self, rng: bool = True):
		super().__init__(name = self.name, dice = self.dice, rng = rng)

class BARD(game_class):
	name		= 'bard'
	dice		= [[1, 8], [5, 1]]
	def __init__(self, rng: bool = True):
		super().__init__(name = self.name, dice = self.dice, rng = rng)

class CLERIC(game_class):
	name 		= 'cleric'
	dice		= [[1, 8], [5, 1]]
	def __init__(self, rng: bool = True):
		super().__init__(name = self.name, dice = self.dice, rng = rng)

class DRUID(game_class):
	name		= 'druid'
	dice		= [[1, 8], [5, 1]]
	def __init__(self, rng: bool = True):
		super().__init__(name = self.name, dice = self.dice, rng = rng)

class FIGHTER(game_class):
	name		= 'fighter'
	dice		= [[1, 10], [6, 1]]
	def __init__(self, rng: bool = True):
		super().__init__(name = self.name, dice = self.dice, rng = rng)

class MONK(game_class):
	name		= 'monk'
	dice		= [[1, 8], [5, 1]]
	def __init__(self, rng: bool = True):
		super().__init__(name = self.name, dice = self.dice, rng = rng)

class PALADIN(game_class):
	name		= 'paladin'
	dice		= [[1, 10], [6, 1]]
	def __init__(self, rng: bool = True):
		super().__init__(name = self.name, dice = self.dice, rng = rng)

class RANGER(game_class):
	name		= 'ranger'
	dice		= [[1, 10], [6, 1]]
	def __init__(self, rng: bool = True):
		super().__init__(name = self.name, dice = self.dice, rng = rng)

class ROGUE(game_class):
	name		= 'rogue'
	dice		= [[1, 8], [5, 1]]
	def __init__(self, rng: bool = True):
		super().__init__(name = self.name, dice = self.dice, rng = rng)

class SORCERER(game_class):
	name		= 'sorcerer'
	dice		= [[1, 6], [4, 1]]
	def __init__(self, rng: bool = True):
		super().__init__(name = self.name, dice = self.dice, rng = rng)

class WARLOCK(game_class):
	name		= 'warlock'
	dice		= [[1, 8], [5, 1]]
	def __init__(self, rng: bool = True):
		super().__init__(name = self.name, dice = self.dice, rng = rng)

class WIZARD(game_class):
	name		= 'wizard' 
	dice		= [[1, 6], [4, 1]]
	def __init__(self, rng: bool = True):
		super().__init__(name = self.name, dice = self.dice, rng = rng)