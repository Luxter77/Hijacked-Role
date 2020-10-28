#!/usr/bin/env python3																			#
# coding: utf-8																					#
																								#
import pickle, os																				#
																								#
# General																						#
CommandPrefix = r'$'																			# Prefix for the Discord commands.
TOKEN         = r''  																			# Discord Bot Token; Note: if you try to use a user token you will get that account banned. 
PATH          = os.getcwd()  																	# Path where the system will deploy
DB_PATH       = os.path.join(PATH, 'DB')														# Haha python library go brrrr
# Admin staff																					#
DevLab        = []	                                 					                        # Internal use... :shrug: (List of server id's as int)
SUPERUSER     = []									 											# List of superusers (id as int) that will have control over special system commands
# Logs																							# 
LogChan       = []    																			# List of channels (id as int) where to tump logs (TODO: separate ERR_LogChan and Log_LogChan).
LogAdmin      = []					    														# List of users	   (id as int) to ping when an error cours (will "try:" to log to LogChan).
# Exclude Lists																					#
GildExList    = []  																			# List of guilds   (!!!)(id as int) excluded from roll system.
ChanExList    = []  																			# List of users    (!!!)(id as int) excluded from roll system.
UserExLixt    = []  																			# List of channels (???)(id as int) excluded from roll system.
# Roll																							#
RolVChan      = []										  										# List of voice channels (id as int) where to execute the Roll_DB subsystem
																								#
def saveConfig():																				# Save the configuration to a file for persistence
	pickle.dump(																				#
		tuple((CommandPrefix, TOKEN, PATH, DB_PATH, DevLab, SUPERUSER, LogChan, LogAdmin,		#
			GildExList, ChanExList, UserExLixt, RolVChan)),										#
			open("Config.pkl", "wb")															#
	)																							#
																								#
# Why do I keep doing this to myself															#
if __main__ == __name__:																		#
	saveConfig()																				#