#!/usr/bin/env python3
# coding: utf-8
from hijackedrole import gclasses
from hijackedrole import dgamer

import random

#TODO: perhaps some day...
#if( not('discord_integration' in globals()) ):
#    import sys
#    discord_integration = True if('discord' in sys.modules) else False
#
#if(discord_integration):
#	from hijackedrole import dgamer 
#else:
#	from hijackedrole import ngamer

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
	def __init__(self, name: str, alighn: list = [], stats: char_stats = None, gaem_class: gclasses.game_class = None):
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

class campaing:
	'''A place where the game concurs, the state is kept'''
	def __init__(self, name: str, GM_: dgamer.gamer, description: str = "What title says", notes: list = [], gamers: list = [], characters: list = []):
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