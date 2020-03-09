#! /usr/bin/python3

###############################################################################
# main.py
# Budg
# by Kyle Bouwman
# subject to MIT License (see LICENSE)
#
# The main script that runs during an instance of the program
###############################################################################

import sys
import os
import budg.console as console

# function handles input errors
def usage_error():
    print("Usage: budget XXX.XX")
    print("Invalid Argument")
    exit(1)

# too many args
if len(sys.argv) > 2:
    usage_error()

USERHOME = os.path.expanduser('~')
CONFIGLOC = os.path.join(USERHOME, ".config/budg")
USERCONFIG = os.path.join(CONFIGLOC, "budget.ini")
DEFCONFIG = os.path.join(CONFIGLOC, "defaultbudget.ini")
CONFIG = None

# check for user config
if os.path.isfile(USERCONFIG):
    CONFIG = USERCONFIG
elif os.path.isfile(DEFCONFIG):
    CONFIG = DEFCONFIG
else:
    print("Config not found")
    exit(2)

#TODO interactive mode
if len(sys.argv) == 1:
    bconsole = console.BudgConsole(CONFIG)