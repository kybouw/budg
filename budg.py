#! /usr/bin/python3

################################################################################
# budget.py
# by Kyle Bouwman
# subject to MIT License (see LICENSE)
#
# This is a script that helps me figure out how to budget my paychecks.
################################################################################

# imports
import configparser
import os.path
from os import system
import sys

# function that handles input errors
def usage_error():
    print('Usage: budget XXX.XX')
    print('Invalid argument')
    exit(1)
    
# verify args
if len(sys.argv) > 2:
    usage_error()

# The console object
class BudgConsole(object):

    # Constructor
    def __init__(self):
        # clear the screen and welcome the user
        system('clear')
        print('Welcome to the Budg Console\n\n')
        # start the console session
        self.startSession()

    # method that runs the session
    def startSession(self):
        # session loop
        sessionIsActive = True
        while sessionIsActive:
            # get user input
            cmd = input("budg> ")
            # 'exit' command breaks the loop
            if cmd == "exit":
                sessionIsActive = False
            # DEBUG this just prints the input out
            print(cmd)

# see if user wants interactive mode
if len(sys.argv) == 1:
    console = BudgConsole()
    exit(0)

# create vars
HOME = os.path.expanduser('~')
USERCONFIG = os.path.join(HOME, '.config/budg/budget.ini')
DEFCONFIG = os.path.join(HOME, '.config/budg/defaultbudget.ini')

# make sure that arg is a float
try:
    AMOUNT = float(sys.argv[1])
except:
    usage_error()

# parse config
config = configparser.ConfigParser()
# if config file already exists
if os.path.isfile(USERCONFIG):

    # then load the file
    config.read(USERCONFIG)

# if config file does not exist
else:

    # use default budget, if present
    if os.path.isfile(DEFCONFIG):
        config.read(DEFCONFIG)
    else:
        print("No config is found. Please create one in ~/.config/budg/")
        exit(2)

# go through categories in config
for section in config.sections():
    print(section)
    for category in config[section]:
        # calculate and show budget for category
        val = float(config[section][category]) * AMOUNT / 102
        txt = "  {}        ${:.2f}"
        print(txt.format(category, val))
