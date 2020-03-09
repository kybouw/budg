#! /usr/bin/python3

###############################################################################
# budg.py
# Budg
# by Kyle Bouwman
# subject to MIT License (see LICENSE)
#
# This is a script that helps me figure out how to budget my paychecks.
###############################################################################

# imports
import configparser
import os
import sys


# function that handles input errors
def usage_error():
    print('Usage: budget XXX.XX')
    print('Invalid argument')
    exit(1)


# verify args
if len(sys.argv) > 2:
    usage_error()


# create vars
HOME = os.path.expanduser('~')
USERCONFIG = os.path.join(HOME, '.config/budg/budget.ini')
DEFCONFIG = os.path.join(HOME, '.config/budg/defaultbudget.ini')
CONFIG = None

# check for user config, try default config, exit in shame
if os.path.isfile(USERCONFIG):
    CONFIG = USERCONFIG

elif os.path.isfile(DEFCONFIG):
    CONFIG = DEFCONFIG

else:
    print("Config not found")
    exit(2)

# see if user wants interactive mode
if len(sys.argv) == 1:
    console = BudgConsole(CONFIG)
    exit(0)

# make sure that arg is a float
try:
    AMOUNT = float(sys.argv[1])
except ValueError:
    usage_error()

# parse config
config = configparser.ConfigParser()
config.read(CONFIG)

# go through categories in config
for section in config.sections():
    print(section)

    for category in config[section]:
        # calculate and show budget for category
        val = float(config[section][category]) * AMOUNT / 102
        # format and print output
        txt = "  {}        ${:.2f}"
        print(txt.format(category, val))
