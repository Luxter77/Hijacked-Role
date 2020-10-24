#!/usr/bin/env python3
# coding: utf-8
from tqdm.asyncio import tqdm as asynctqdm
from discord.ext import commands
from tqdm.auto import tqdm

import datetime as dt
import traceback, discord
import asyncio, pickle
import glob, sys, os, re

import config

from misc import *


print(os.getcwd())
# Load
CommandPrefix, TOKEN, PATH, DB_PATH, DevLab, SUPERUSER, LogChan, LogAdmin, GildExList, ChanExList, UserExLixt, RolVChan = pickle.load(open('Config.pkl', 'rb'))

# init
bot = commands.Bot(command_prefix=CommandPrefix, case_insensitive=True)
slash = "\\" if (os.name == 'nt') else "/" # Where the heck am I
os.makedirs(DB_PATH, exist_ok=True)

## All of this was carried over from Hijacked Node
async def logMe(st, err_ = False, tq = True):
	if(err_):
		_stderr = '|-----------------ERR_ START-------------------|'
		print(_stderr) if(tq) else tqdm.write(_stderr)
		print(st) if(tq) else tqdm.write(st)
		try:
			for Chan in LogChan:
				await bot.get_channel(Chan).send('|-----------------ERR_ START-------------------|')
				await bot.get_channel(Chan).send(' '.join([("<@" + str(admin[0]) + ">:") for admin in LogAdmin]))
				await bot.get_channel(Chan).send(st)
				await bot.get_channel(Chan).send('|------------------ERR_ END--------------------|')
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
			for Chan in LogChan:
				await bot.get_channel(Chan).send(st)

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
async def on_ready():
	await logMe('|-----------------doBootUp-st------------------|')
	await logMe('|           Testing Testing 1, 2, 3            |') #TODO: Think of a cool phrase to replace this one
	await logMe('|----------------------------------------------|')
	await bot.change_presence(activity = discord.Game(name = 'Waking Up...'))
	async with bot.get_channel(LogChan[0]).typing():
		await logMe( "[ " + str(dt.datetime.now().timestamp()) + " ]" )
		await logMe( str(bot.user) + " Is connected to:")
		await logMe('|----------------------------------------------|')
		for guild in bot.guilds:
			await logMe(" - [" + str(guild.id) + "]: " + str(guild.name) + ".")
		await logMe('|----------------------------------------------|')
		await logMe("|           Bootup Sequence complete           |")
		await bot.change_presence(activity = discord.Game(name = 'Soulcasting'))
	await logMe('|----------------doBootUp End------------------|')

### HERE BE DRAGONS;

@bot.command(pass_context=True)
async def ttest(ctx: discord.ext.commands.Context):
	await ctx.send('test')

@bot.group(pass_context=True)
async def aeiou(ctx: discord.ext.commands.Context):
	if ctx.invoked_subcommand is None:
		await ctx.send('Invalid sub command')

@aeiou.command(pass_context=True)
async def test(ctx: discord.ext.commands.Context):
	await ctx.send("test")

### DRAGONS END HERE;
### Tarasques ahead
bot.run(TOKEN)