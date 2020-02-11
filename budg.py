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

# The console object
class BudgConsole(object):

    # Constructor
    def __init__(self, config):

        # set the config
        self.configfile = config
        self.cfgparser = configparser.ConfigParser()
        self.cfgparser.read(self.configfile)

        # clear the screen and welcome the user
        self.clearScreen()
        print('Welcome to the Budg Console\n\n')
        # start the console session
        self.runSession()

    # method that runs the session
    def runSession(self):
        # session loop
        sessionIsActive = True
        while sessionIsActive:
            # get user input
            cmd = input("budg> ")
            # 'exit' command breaks the loop
            if cmd == "exit":
                sessionIsActive = False
            # DEBUG this just prints the input out
            self.readInput(cmd)

    # clears the screen
    def clearScreen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    # interprets the input command
    def readInput(self, cmd):
        consolev = cmd.split()
        if consolev[0] == "pc":
            self.paycheck(consolev[1:])
        else:
            print(consolev)

    def paycheck(self, amounts):
        total = 0.0
        valid = True
        for check in amounts:
            try:
                total += float(check)
            except:
                print("Invalid input")
                valid = False
                break

        if valid == True and total > 0:
            self.printBudget(total)

    def printBudget(self, check):
        for section in self.cfgparser.sections():
            print(section)
            for category in self.cfgparser[section]:
                val = float(self.cfgparser[section][category]) * check / 102
                txt = "  {}        ${:.2f}"
                print(txt.format(category, val))



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
except:
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
        txt = "  {}        ${:.2f}"
        print(txt.format(category, val))
