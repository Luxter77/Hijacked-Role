#!/usr/bin/env python3
# coding: utf-8
class game_class():
	"TODO: Make it so there are other classes"
	"for now, just DnD classes"
	def __init__(self, name: str, savthrow: list, _HPDICE: list, _CNDICE: list, class_level: int = 1, rng: bool = True):
		self.name			= name
		self.savthrow		= savthrow
		self._HPDICE		= _HPDICE
		self._CNDICE		= _CNDICE
		self.rng			= rng
		self.class_level	= class_level
	def __str__(self):
		return(self.name)

class BARBARIAN(game_class):
	name 		= 'barbarian'
	savthrow	= ['stre', 'conn']
	_HITICE		= 12
	_HPDICE		= [1, 12]
	_UPDICE 	= [[1, 12], [7, 1]]
	def __init__(self, name: str, savthrow: list, _HPDICE: list, _CNDICE: list, rng: bool = True):
		super().__init__(self.name, self.savthrow, self._HPDICE, self._CNDICE, self.rng)

class BARD(game_class):
	name		= 'bard'
	savthrow	= ['conn', 'char']
	_HITICE		= 8
	_HPDICE		= [8, 1]
	_UPDICE		= [[1, 8], [5, 1]]
	def __init__(self, name: str, savthrow: list, _HPDICE: list, _CNDICE: list, rng: bool = True):
		super().__init__(self.name, self.savthrow, self._HPDICE, self._CNDICE, self.rng)

class CLERIC(game_class):
	name 		= 'cleric'
	savthrow	= ['wisd', 'char']
	_HITICE		= 8
	_HPDICE		= [8, 1]
	_UPDICE		= [[1, 8], [5, 1]]
	def __init__(self, name: str, savthrow: list, _HPDICE: list, _CNDICE: list, rng: bool = True):
		super().__init__(self.name, self.savthrow, self._HPDICE, self._CNDICE, self.rng)

class DRUID(game_class):
	name		= 'druid'
	savthrow	= ['inte', 'wisd']
	_HITICE		= 8
	_HPDICE		= [8, 1]
	_UPDICE		= [[1, 8], [5, 1]]
	def __init__(self, name: str, savthrow: list, _HPDICE: list, _CNDICE: list, rng: bool = True):
		super().__init__(self.name, self.savthrow, self._HPDICE, self._CNDICE, self.rng)

class FIGHTER(game_class):
	name		= 'fighter'
	savthrow	= ['stre', 'conn']
	_HITICE		= ['conn', 10]
	_HPDICE		= [10, 1]
	_UPDICE		= [[1, 10], [6, 1]]
	def __init__(self, name: str, savthrow: list, _HPDICE: list, _CNDICE: list, rng: bool = True):
		super().__init__(self.name, self.savthrow, self._HPDICE, self._CNDICE, self.rng)

class MONK(game_class):
	name		= 'monk'
	savthrow	= ['', '']
	_HITICE		= int
	_HPDICE		= [int, int]
	_UPDICE		= [[int, int], [int, int]]
	def __init__(self, name: str, savthrow: list, _HPDICE: list, _CNDICE: list, rng: bool = True):
		super().__init__(self.name, self.savthrow, self._HPDICE, self._CNDICE, self.rng)

class PALADIN(game_class):
	name		= 'paladin'
	savthrow	= ['', '']
	_HITICE		= int
	_HPDICE		= [int, int]
	_UPDICE		= [[int, int], [int, int]]
	def __init__(self, name: str, savthrow: list, _HPDICE: list, _CNDICE: list, rng: bool = True):
		super().__init__(self.name, self.savthrow, self._HPDICE, self._CNDICE, self.rng)

class RANGER(game_class):
	name		= 'ranger'
	savthrow	= ['', '']
	_HITICE		= int
	_HPDICE		= [int, int]
	_UPDICE		= [[int, int], [int, int]]
	def __init__(self, name: str, savthrow: list, _HPDICE: list, _CNDICE: list, rng: bool = True):
		super().__init__(self.name, self.savthrow, self._HPDICE, self._CNDICE, self.rng)

class ROGUE(game_class):
	name		= 'rogue'
	savthrow	= ['', '']
	_HITICE		= int
	_HPDICE		= [int, int]
	_UPDICE		= [[int, int], [int, int]]
	def __init__(self, name: str, savthrow: list, _HPDICE: list, _CNDICE: list, rng: bool = True):
		super().__init__(self.name, self.savthrow, self._HPDICE, self._CNDICE, self.rng)

class SORCERER(game_class):
	name		= 'sorcerer'
	savthrow	= ['', '']
	_HITICE		= int
	_HPDICE		= [int, int]
	_UPDICE		= [[int, int], [int, int]]
	def __init__(self, name: str, savthrow: list, _HPDICE: list, _CNDICE: list, rng: bool = True):
		super().__init__(self.name, self.savthrow, self._HPDICE, self._CNDICE, self.rng)

class WARLOCK(game_class):
	name		= 'warlock'
	savthrow	= ['', '']
	_HITICE		= int
	_HPDICE		= [int, int, '']
	_UPDICE		= [[int, int, ''], [int, int, '']]
	def __init__(self, name: str, savthrow: list, _HPDICE: list, _CNDICE: list, rng: bool = True):
		super().__init__(self.name, self.savthrow, self._HPDICE, self._CNDICE, self.rng)

class WIZARD(game_class):
	name		= 'wizard'
	savthrow	= ['', '']
	_HITICE		= int
	_HPDICE		= [int, int, '']
	_UPDICE		= [[int, int, ''], [int, int, '']]
	def __init__(self, name: str, savthrow: list, _HPDICE: list, _CNDICE: list, rng: bool = True):
		super().__init__(self.name, self.savthrow, self._HPDICE, self._CNDICE, self.rng)
