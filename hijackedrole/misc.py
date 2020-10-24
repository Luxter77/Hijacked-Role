#!/usr/bin/env python3
# coding: utf-8
from hijackedrole import dgamer
from hijackedrole import characters

class game_object:
	'''A thing that a character can have or equip or use'''
	def __init__(self, name: str,  stats: characters.char_stats, description: str = "What title says", equipable: bool = False, isequiped: bool = False, usable: bool = False, isAmmo: bool = False, ammount: int = 1):
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