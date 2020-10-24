#!/usr/bin/env python3
# coding: utf-8
import discord
import random

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

class char_stats:
	'''
	strength		(strg): How much you strong,\n
	inteligence 	(inte): How much you think,\n
	speed			(sped): How fast you move,\n
	dexterity		(dext): How well you move,\n
	wisdom			(wisd):	How well you think,\n
	constitution	(conn):	How well you,\n
	carisma			(char): How nice you,\n
	luck 			(luck): How well you,\n
	seed			(seed): How.
	'''
	def __init__(self, strg: int = 10, inte: int = 10, sped: int = 10, dext: int = 10, wisd: int = 10, conn: int = 10, char: int = 10, luck: int = 50, levl: int = 1, seed: int = None):
		self.strg = strg
		self.inte = inte
		self.sped = sped
		self.dext = dext
		self.wisd = wisd
		self.conn = conn
		self.char = char
		self.luck = luck
		self.levl = levl
		self.seed = seed if(seed) else random.randint(-65535, 65536)
	def __str__(self):
		return(	
			'Stats:           '	+
			'\n   str:          '	+ str(self.strg) +
			'\n   int:          '	+ str(self.inte) +
			'\n   spd:          '	+ str(self.sped) +
			'\n   dex:          '	+ str(self.dext) +
			'\n   wis:          '	+ str(self.wisd) +
			'\n   con:          '	+ str(self.conn) +
			'\n   chr:          '	+ str(self.char) +
			'\n   luck:         '	+ str(self.luck) +
			'\n   level:        '	+ str(self.levl) +
			'\n   magic number: '	+ str(self.seed)
		)

class char_state:
	'TODO: *'
	def __init__(self, MaxHP: int = 5):
		self.MaxHP	= MaxHP
		self.HP		= MaxHP

class game_object:
	'''A thing that a character can have or equip or use'''
	def __init__(self, name: str,  stats: char_stats, description: str = "What title says", equipable: bool = False, isequiped: bool = False, usable: bool = False, isAmmo: bool = False, ammount: int = 1):
		self.name			= name
		self.stats			= stats
		self.description	= description
		self.equipable		= equipable
		self.isequiped		= isequiped
		self.usable			= usable
		self.isAmmo			= isAmmo
		self.ammount		= ammount
	def __str__(self):
		return( '<' + self.name + '>\n[ ' + str(self.description) + ' ]\n' + 'Stats:\n' + str(self.stats) + '\n' + (('This object is equipable.\n') if(self.equipable) else '') + (('This object is usable.\n') if(self.usable) else '') + (('This object is ammo.\n') if(self.equipable) else '') )

class character:
	"""Playable character, OC, if you will"""
	def __init__(self, name: str, alighn: list = [], stats: char_stats = None, gaem_class: game_class = None):
		self.name		= name
		self.alighn		= alighn
		self.stats		= stats
		self.state		= char_state()
		self.gaem_class	= gaem_class
		self.inventory	= []
	def addobject(self, _object: game_object):
		self.inventory.append(_object)
	def delobject(self, id_: int):
		self.inventory.remove(id_-1)
	def listobjects(self):
		return((( str(i) + ')) <' + self.inventory[i].name + '>::<' + str(self.inventory[i].ammount) + '>\n') for i in range(len(self.inventory))))
	def __str__(self):
		return( '<' + self.name + '>\n Class: ' + str(self.gaem_class.name) )
	def damage(self, dmg_int: int = 1, true = False):
		if(true):
			self.state.HP -= dmg_int

class gamer:
	'''Thing that plays and happens to be a discord user'''
	def __init__(self, user: discord.User, chars: dict = {}, rollingAs: character = None, isRolling: bool = False, isGM: bool = False):
		self.user		= user          # Discord user, holds _a lot_ of data

		self.chars      = chars         # dict of characters by id (TODO: what is an id?)
		
		self.isRolling  = isRolling     # is this user engaging in roleplay now?
		self.rollingAs  = rollingAs     # if this user is rolling as someone, as who?
		self.isGM		= isGM          # is this user a Game Master?

	def __str__(self):
		return(
			'<' + str(self.user.name) + '>::<' + str(self.user.id) + '>\n' +
			('This player is a GM\n' if(self.isGM) else '') +
			(('This player has the following characters:' + '\n'.join([x for x in self.chars])) if (self.chars) else ('This player has no characters')) +
			(('This player is rolling as: ' + self.rollingAs + '\n') if (self.isRolling and bool(self.chars)) else '')
		)

class campaing:
	'''A place where the game concurs, the state is kept'''
	def __init__(self, name: str, GM_: gamer, description: str = "What title says", notes: list = [], gamers: list = [], characters: list = []):
		self.name			= name
		self.description	= description
		self.notes			= notes
		self.gamers			= gamers
		self.GM				= GM_
	def __str__(self):
		return(
			self.name				+ ':\n '				+
			self.description		+ '\n\n Game Master: '	+
			str(self.GM.mention)	+ '\n'					+
			' Players: ' + '\n   '.join([((str(gamer.mention))) for gamer in self.gamers])
		)
	def getNotes(self):
		return('\n'.join(self.notes))
	def addNote(self, msg: str):
		self.notes.append(msg)
	def delNote(self, id_:  int):
		self.notes.remove(id_)