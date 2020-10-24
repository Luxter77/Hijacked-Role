#!/usr/bin/env python3
# coding: utf-8
class game_class():
	"TODO: Make it so there are other classes"
	"for now, just DnD classes"
	def __init__(self, name: str, save: list, dice: list, clvl: int = 1, rng: bool = True):
		self.name			= name
		self.save			= save
		self.dice			= dice
		self.clvl			= clvl
		self.rng			= rng
	def __str__(self):
		return('<' + self.name + '>::<' + str(self.clvl) + '>')

class BARBARIAN(game_class):
	name 		= 'barbarian'
	save		= ['stre', 'conn']
	dice		= [[1, 12], [7, 1]]
	def __init__(self, name: str, save: list, dice: list, rng: bool = True):
		super().__init__(self.name, self.save, self.dice, self.rng)

class BARD(game_class):
	name		= 'bard'
	save		= ['conn', 'char']
	dice		= [[1, 8], [5, 1]]
	def __init__(self, name: str, save: list, dice: list, rng: bool = True):
		super().__init__(self.name, self.save, self.dice, self.rng)

class CLERIC(game_class):
	name 		= 'cleric'
	save		= ['wisd', 'char']
	dice		= [[1, 8], [5, 1]]
	def __init__(self, name: str, save: list, dice: list, rng: bool = True):
		super().__init__(self.name, self.save, self.dice, self.rng)

class DRUID(game_class):
	name		= 'druid'
	save		= ['inte', 'wisd']
	dice		= [[1, 8], [5, 1]]
	def __init__(self, name: str, save: list, dice: list, rng: bool = True):
		super().__init__(self.name, self.save, self.dice, self.rng)

class FIGHTER(game_class):
	name		= 'fighter'
	save		= ['stre', 'conn']
	dice		= [[1, 10], [6, 1]]
	def __init__(self, name: str, save: list, dice: list, rng: bool = True):
		super().__init__(self.name, self.save, self.dice, self.rng)

class MONK(game_class):
	name		= 'monk'
	save		= ['', '']
	dice		= [[int, int], [int, int]]
	def __init__(self, name: str, save: list, dice: list, rng: bool = True):
		super().__init__(self.name, self.save, self.dice, self.rng)

class PALADIN(game_class):
	name		= 'paladin'
	save		= ['', '']
	dice		= [[int, int], [int, int]]
	def __init__(self, name: str, save: list, dice: list, rng: bool = True):
		super().__init__(self.name, self.save, self.dice, self.rng)

class RANGER(game_class):
	name		= 'ranger'
	save		= ['', '']
	dice		= [[int, int], [int, int]]
	def __init__(self, name: str, save: list, dice: list, rng: bool = True):
		super().__init__(self.name, self.save, self.dice, self.rng)

class ROGUE(game_class):
	name		= 'rogue'
	save		= ['', '']
	dice		= [[int, int], [int, int]]
	def __init__(self, name: str, save: list, dice: list, rng: bool = True):
		super().__init__(self.name, self.save, self.dice, self.rng)

class SORCERER(game_class):
	name		= 'sorcerer'
	save		= ['', '']
	dice		= [[int, int], [int, int]]
	def __init__(self, name: str, save: list, dice: list, rng: bool = True):
		super().__init__(self.name, self.save, self.dice, self.rng)

class WARLOCK(game_class):
	name		= 'warlock'
	save		= ['', '']
	dice		= [[int, int], [int, int]]
	def __init__(self, name: str, save: list, dice: list, rng: bool = True):
		super().__init__(self.name, self.save, self.dice, self.rng)

class WIZARD(game_class):
	name		= 'wizard' 
	save		= ['', '']
	dice		= [[int, int], [int, int]]
	def __init__(self, name: str, save: list, dice: list, rng: bool = True):
		super().__init__(self.name, self.save, self.dice, self.rng)
