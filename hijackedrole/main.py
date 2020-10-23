#!/usr/bin/env python3
# coding: utf-8
# import I don't know how to use python packages
from hijacked_role import game_classes
import random
import sys

discord_integration = True if('discord' in sys.modules) else False

class char_stats:
	'''
	stats, if you will.
	strength		(strg): How much you strong,
	inteligence 	(inte): How much you think,
	speed			(sped): How fast you move,
	dexterity		(dext): How well you move,
	wisdom			(wisd):	How well you think,
	constitution	(conn):	How well you,
	carisma			(char): How nice you,
	luck 			(luck): How well you,
	seed			(seed): How
	'''
	def __init__(self, strg: int = 10, inte: int = 10, sped: int = 10, dext: int = 10, wisd: int = 10, conn: int = 10, char: int = 10, luck: int = 50, levl: int = 1, seed: int = None):
		self.strg			= strg
		self.inte			= inte
		self.sped			= sped
		self.dext			= dext
		self.wisd			= wisd
		self.conn			= conn
		self.char			= char
		self.luck			= luck
		self.levl			= levl
		self.seed 			= seed if(seed) else random.randint(-65535, 65536)
	def __str__(self):
		return(	'Stats:' +
			'\n str: '   + str(self.strg) +
			'\n int: '   + str(self.inte) +
			'\n spd: '   + str(self.sped) +
			'\n dex: '   + str(self.dext) +
			'\n wis: '   + str(self.wisd) +
			'\n con: '   + str(self.conn) +
			'\n chr: '   + str(self.char) +
			'\n luck: '  + str(self.luck) +
			'\n level: ' + str(self.levl) +
			'\n magic: ' + str(self.seed)
		)

class character_state:
	def __init__(self):
		print('')

class game_object:
	'''A thing that a character can have or equip or use'''
	def __init__(self, id_, name: str,  stats: char_stats, description: str = "What title says", equipable: bool = False, isequiped: bool = False, usable: bool = False, isammo: bool = False, cuantity: int = 1):
		self.id				= id_
		self.name			= name
		self.stats			= stats
		self.description	= description
		self.equipable		= equipable
		self.isequiped		= isequiped
		self.usable			= usable
		self.isammo			= isammo
		self.cuantity		= cuantity
	def __str__(self):
		return( '<' + str(self.id) + '>::<' + self.name + '>\n[ ' + str(self.description) + ' ]\n' + 'Stats:\n' + str(self.stats) + '\n' + (('This object is equipable.\n') if(self.equipable) else '') + (('This object is usable.\n') if(self.usable) else '') + (('This object is ammo.\n') if(self.equipable) else '') )

class character:
	"""Playable character, OC, if you will"""
	def __init__(self, name: str, id_: int, alighn: list = [], stats: char_stats = None, gaem_class: game_class = None):
		self.name		= name
		self.id			= id_
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
		return((( str(i) + ')) <' + self.inventory[i].name + '>::<' + str(self.inventory[i].cuantity) + '>\n') for i in range(len(self.inventory))))
	def __str__(self):
		return( '<' + (self.id) + '>::<' + self.name + '>\n Class: ' + str(self.gaem_class.name) )
	def damage(self, dmg_int: int = 1, true = False):
		if(true):
			self.state.HP -= dmg_int

class gamer:
	'''thing that plays'''
	def __init__(self, id_: int, characters: dict = {}, rollingas: character = None, isrolling: bool = False, isgm: bool = False, _lusedname: str = 'NDP_NAME_ERROR'):
		self.id	        = id_
		self.characters = characters
		self.rollingas  = rollingas
		self.isrolling  = isrolling
		self.isgm		= isgm
		self._lusedname	= _lusedname
	def __str__(self):
		return( '<' + str(self.id) + '>::<' + self._lusedname + '>\n' + (('Rolling as: ' + self.rollingas.name + '\n') if(self.isrolling) else '') + ('This player is a GM' if(self.isgm) else '') )

class campaing:
	'''A place where the game concurs, the state is kept'''
	def __init__(self, id_: int, name: str, description: str = "What title says", notes: str = "", gamers: list = [], GM_: gamer = None, characters: list = []):
		self.id				= id_
		self.name			= name
		self.description	= description
		self.notes			= notes
		self.gamers			= gamers
		self.GM				= GM_
	def __str__(self):
		return( '<' + str(self.id) + '>::<' + self.name + '>\n' + self.description + '\nGM: ' + (('<@' + str(self.GM.id) + '>') if (discord_integration) else (str(self.GM._lusedname))))

print('didnt explode')
