#!/usr/bin/env python3
# coding: utf-8
import discord

from hijackedrole import characters

class gamer:
	'''Thing that plays and happens to be a discord user'''
	def __init__(self, user: discord.User, chars: dict = {}, rollingAs: characters.character = None, isRolling: bool = False, isGM: bool = False):
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