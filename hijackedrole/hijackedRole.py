#!/usr/bin/env python3
# coding: utf-8
from tqdm.asyncio import tqdm as asynctqdm
from discord.ext import commands
from tqdm.auto import tqdm

import datetime as dt
import traceback, discord
import asyncio, pickle
import glob, sys, os, re

try:
	from hijackedrole import config
except:
	try:
		class CONF0():
			def __init__(self, conf):
				self.CommandPrefix, self.TOKEN, self.PATH, self.DB_PATH, self.DevLab, self.SUPERUSER, self.LogChan, self.LogAdmin, self.GildExList, self.ChanExList, self.UserExLixt, self.RolVChan = conf
			config = CONF0(tuple(pickle.load(open("Config.pkl", "wb"))))	
	except:
		print("I can't find configurations, now exiting")

from hijackedrole import mis_

# init
bot = commands.Bot(command_prefix=config.CommandPrefix, case_insensitive=True)
os.makedirs(config.DB_PATH, exist_ok=True)

## All of this was carried over from Hijacked Node
async def logMe(st, err_ = False, tq = True):
	if(err_):
		_stderr = '|-----------------ERR_ START-------------------|'
		print(_stderr) if(tq) else tqdm.write(_stderr)
		print(st) if(tq) else tqdm.write(st)
		try:
			for Chan in config.LogChan:
				await bot.get_channel(Chan).send('|-----------------ERR_ START-------------------|')
				await bot.get_channel(Chan).send(' '.join([("<@" + str(admin) + ">:") for admin in config.LogAdmin]))
				await bot.get_channel(Chan).send(st)
				await bot.get_channel(Chan).send('|------------------ERR_ END--------------------|')
		except:
			try:
				for Chan in config.LogChan:
					await bot.get_channel(Chan).send('|--------------- ERR_ START ----------------|')
					try:
						await bot.get_channel(Chan).send("<@" + str(config.LogAdmin[0]) + ">:")
						await bot.get_channel(Chan).send(str(st))
					except:
						await bot.get_channel(Chan).send("<@" + str(config.LogAdmin[0]) + ">:")
						await bot.get_channel(Chan).send("Some unprinteable error happened... ")
					await bot.get_channel(Chan).send('|------------------ERR_ END--------------------|')
			except:
				_stderr = "Ah for hugs sake something went horribly grong! AGAIN"
				print(_stderr) if(tq) else tqdm.write(_stderr)
		_stderr = '|------------------ERR_ END--------------------|'
		print(_stderr) if(tq) else tqdm.write(_stderr)
	else:
		_stdout = st
		print(_stdout) if(tq) else tqdm.write(_stdout)
		try:
			for Chan in config.LogChan:
				await bot.get_channel(Chan).send(st)

		except:
			try:
				for Chan in config.LogChan:
					try:
						try:
							await bot.get_channel(Chan).send(st)
						except:
							await bot.get_channel(Chan).send(str(st))
					except:
						await bot.get_channel(Chan).send("Some unprinteable error happened... ")
			except:
				await bot.get_channel(Chan).send('|------------------Log_ START------------------|')
				await logMe("Ah for fucks sake something went horribly grong!", True)
				await bot.get_channel(Chan).send('|------------------Log_ END--------------------|')

@bot.event
async def on_command_error(context, exception):
    print('|--------------- ERR_ START ----------------|')
    print('Ignoring exception in command {}:'.format(context.command), file=sys.stderr)
    traceback.print_exception(type(exception), exception, exception.__traceback__, file=sys.stderr)
    print('|---------------- ERR_ END -----------------|')
    try:
        await logMe(context.message.content)
    except:
        None
    try: 
        await logMe(exception, True)
    except:
        None

@bot.event
async def on_error(event_method, *args, **kwargs):
	try:
		await logMe(" ``` "	+	event_method			+	" ``` ", True)
		await logMe(" ``` "	+	traceback.format_exc()	+	" ``` ", True)
	except:
		print('|------------------ERR_ START------------------|')
		print(' Ignoring exception in {}'.format(event_method), file=sys.stderr)
		traceback.print_exc()
		print('|------------------ ERR_ END ------------------|')

@bot.event
async def on_message(message):
	await EMT(message)
	if(message.author != bot.user):
		await bot.process_commands(message)
		cont = message.content.lower()
		await talk(message, True) if ( not(cont.startswith("--")) and not(cont.startswith("/")) and not(cont.startswith("!")) and not(cont.startswith("$")) and bool(re.search("node", cont))) else None

async def doBootUp(): #spagget
	def sec():
		await logMe( "[ " + str(dt.datetime.now().timestamp()) + " ]" )
		await logMe( str(bot.user) + " Is connected to:")
		await logMe('|----------------------------------------------|')
		for guild in bot.guilds:
			await logMe(" - [" + str(guild.id) + "]: " + str(guild.name) + ".")
		await logMe('|----------------------------------------------|')
		await logMe("|           Bootup Sequence complete           |")
		#await genDB(config.DB_PATH)
		#await CONN_V([], init = True)
		await bot.change_presence(activity = discord.Game(name = 'Soulcasting'))
	await logMe('|-----------------doBootUp-st------------------|')
	await logMe('|           Testing Testing 1, 2, 3            |') #TODO: Think of a cool phrase to replace this one
	await logMe('|----------------------------------------------|')
	await bot.change_presence(activity = discord.Game(name = 'Waking Up...'))
	if(LogChan):
		async with bot.get_channel(LogChan[0]).typing():
			await sec()
	else:
		await sec()
	await logMe('|----------------doBootUp End------------------|')

@bot.event
async def on_ready():
	await doBootUp()

### HERE BE DRAGONS;
#@bot.command(pass_context=True, brief='', description='')

@bot.group(pass_context=True, brief='Role System Command', description='Controls everything related roleplay mechanincs and meta')
async def role(ctx: discord.ext.commands.Context):
	if ctx.invoked_subcommand is None:
		await ctx.send('')

@role.group(pass_context=True, brief='Creates a new instance', description='Creates a new instance of the given object')
async def new(ctx: discord.ext.commands.Context):
	await ctx.send('aeiouaeiouaeiou')

@new.group(pass_context=True)
async def character(ctx: discord.ext.commands.Context):
	if(ctx.author in PLAYER_DB.get_players()):
		await ctx.send('')

### DRAGONS END HERE;
### Tarasques ahead
bot.run(config.TOKEN)