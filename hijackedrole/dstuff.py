#!/usr/bin/env python3
# coding: utf-8
## All of this was carried over from Hijacked Node
from tqdm.asyncio import tqdm as asynctqdm
from discord.ext import commands
from tqdm.auto import tqdm
import discord
import asyncio
import pickle
import glob
import sys
import os
import re

async def logMe(st, err_ = False, tq = True):
	if(err_):
		_stderr = '|--------------- ERR_ START ----------------|'
		print(_stderr) if(tq) else tqdm.write(_stderr)
		print(st) if(tq) else tqdm.write(st)
		try:
			for Chan in LogChan:
				await bot.get_channel(Chan).send('|--------------- ERR_ START ----------------|')
				await bot.get_channel(Chan).send("<@" + str(LogAdmin[0]) + ">:")
				await bot.get_channel(Chan).send(st)
				await bot.get_channel(Chan).send('|---------------- ERR_ END -----------------|')
		except:
			try:
				for Chan in LogChan:
					await bot.get_channel(Chan).send('|--------------- ERR_ START ----------------|')
					try:
						await bot.get_channel(Chan).send("<@" + str(LogAdmin[0]) + ">:")
						await bot.get_channel(Chan).send(str(st))
					except:
						await bot.get_channel(Chan).send("<@" + str(LogAdmin[0]) + ">:")
						await bot.get_channel(Chan).send("Some unprinteable error happened... ")
					await bot.get_channel(Chan).send('|---------------- ERR_ END -----------------|')
			except:
				_stderr = "Ah for fucks sake something went horribly grong! AGAIN"
				print(_stderr) if(tq) else tqdm.write(_stderr)
		_stderr = '|---------------- ERR_ END -----------------|'
		print(_stderr) if(tq) else tqdm.write(_stderr)
	else:
		#print('|--------------- Log_ START ----------------|')
		_stdout = st
		print(_stdout) if(tq) else tqdm.write(_stdout)
		try:
			for Chan in LogChan:
				#await bot.get_channel(Chan).send('|--------------- Log_ START ----------------|')
				await bot.get_channel(Chan).send(st)
				#await bot.get_channel(Chan).send('|---------------- Log_ END -----------------|')

		except:
			try:
				for Chan in LogChan:
					try:
						try:
							await bot.get_channel(Chan).send(st)
						except:
							await bot.get_channel(Chan).send(str(st))
					except:
						await bot.get_channel(Chan).send("Some unprinteable error happened... ")
					#await bot.get_channel(Chan).send('|---------------- Log_ END -----------------|')
			except:
				await bot.get_channel(Chan).send('|--------------- Log_ START ----------------|')
				await logMe("Ah for fucks sake something went horribly grong!", True)
				await bot.get_channel(Chan).send('|---------------- Log_ END -----------------|')
		#print('|---------------- Log_ END -----------------|')

@bot.event
async def on_error(event_method, *args, **kwargs):
	try:
		await logMe(" ``` " +   event_method+          +    " ``` ", True)
		await logMe(" ``` " +   traceback.format_exc() +    " ``` ", True)
	except:
		print('|--------------- ERR_ START ----------------|')
		print(' Ignoring exception in {}'.format(event_method), file=sys.stderr)
		traceback.print_exc()
		print('|----------------- ERR_ END -----------------|')

# Not going to be used... yet
#@bot.event
#async def on_message(message):
#	await EMT(message)
#	if(message.author != bot.user):
#		await bot.process_commands(message)
#		cont = message.content.lower()
#		await talk(message, True) if ( not(cont.startswith("--")) and not(cont.startswith("/")) and not(cont.startswith("!")) and not(cont.startswith("$")) and bool(re.search("node", cont))) else None

@bot.event
async def on_ready():
	await logMe('|---------------doBootUp-st-----------------|')
	#await logMe('|Not really an error, but rather an exploit.|') #TODO: Think of a cool phrase to replace this one
	await logMe('|-------------------------------------------|')
	await bot.change_presence(activity = discord.Game(name = 'Waking Up...'))
	async with bot.get_channel(692694533489557525).typing():
		await logMe( "[ " + str(dt.datetime.now().timestamp()) + " ]" )
		await logMe( str(bot.user) + " Is connected to:")
		await logMe('|-------------------------------------------|')
		for guild in bot.guilds:
			await logMe(" - [" + str(guild.id) + "]: " + str(guild.name) + ".")
		await logMe('|-------------------------------------------|')
		await logMe("|         Bootup Sequence complete          |")
		await bot.change_presence(activity = discord.Game(name = 'Casting Fireball'))
	await logMe('|-------------- doBootUp End ---------------|')