##!/usr/bin/env ipython3
# coding: utf-8
from tqdm.asyncio import tqdm as asynctqdm
from discord.ext import commands
from discord.ext import buttons
from tqdm.auto import tqdm

import datetime as dt
import traceback
import argparse
import discord
import asyncio
import random
import pickle
import glob
import sys
import os
import re

from hijackedrole.config import getConfig, getCDB, getPDB
from hijackedrole.logger import LogMe

# Why do I keep doing this to myself
config = getConfig()
bot = commands.Bot(command_prefix=config.CommandPrefix, case_insensitive=True)
os.makedirs(config.DB_PATH, exist_ok=True)

# All of this was carried over from Hijacked Node
@bot.event
async def on_command_error(context, exception):
    print('|--------------- ERR_ START ----------------|')
    print('Ignoring exception in command {}:'.format(context.command),
          file=sys.stderr)
    traceback.print_exception(type(exception),
                              exception,
                              exception.__traceback__,
                              file=sys.stderr)
    print('|---------------- ERR_ END -----------------|')
    try:
        await logMe(context.message.content)
    except Exception:
        None
    try:
        await logMe(exception, True)
    except Exception:
        None

@bot.event
async def on_error(event_method, *args, **kwargs):
    try:
        await logMe(" ``` " + event_method + " ``` ", True)
        await logMe(" ``` " + traceback.format_exc() + " ``` ", True)
    except Exception:
        print('|------------------ERR_ START------------------|')
        print(' Ignoring exception in {}'.format(event_method), file=sys.stderr)
        traceback.print_exc()
        print('|------------------ ERR_ END ------------------|')

async def doBootUp():  # spagget
    # Set up logging facility
    global logMe
    logMe = LogMe(bot, config)

    # Initialize stuff
    await logMe('|-----------------doBootUp-st------------------|')
    await logMe('|           Testing Testing 1, 2, 3            |')
    await logMe('|----------------------------------------------|')
    await bot.change_presence(activity=discord.Game(name='Waking Up...'))
    await logMe("[ " + str(dt.datetime.now().timestamp()) + " ]")
    await logMe(str(bot.user) + " Is connected to:")
    await logMe('|----------------------------------------------|')
    for guild in bot.guilds:
        await logMe(" - [" + str(guild.id) + "]: " + str(guild.name) + ".")
    global PDB
    global CDB
    PDB = await getPDB()
    CDB = await getCDB()
    await logMe('|----------------------------------------------|')
    await logMe("|           Bootup Sequence complete           |")
    await logMe('|----------------------------------------------|')
    await bot.change_presence(activity=discord.Game(name='Soulcasting'))
    await logMe('|----------------doBootUp End------------------|')

@bot.event
async def on_ready():
    await doBootUp()

# HERE BE DRAGONS;
# @bot.command(pass_context=True, brief='', description='')
