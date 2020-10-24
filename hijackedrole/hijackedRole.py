#!/usr/bin/env python3
# coding: utf-8
from discord.ext import commands
import discord
import random
import sys
import os

CommandPrefix = '!role'


# init
bot = commands.Bot(command_prefix=CommandPrefix, case_insensitive=True)
global slash
slash = "\\" if (os.name == 'nt') else "/" # Where the heck am I

#debug info
global debugTrigger
debugTrigger = False # It prints stuff

