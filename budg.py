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
import sys

# verify args
if len(sys.argv) != 2:
    print('Usage: budget XXX.XX')
    print('Invalid argument')
    exit(1)

# create vars
HOME = os.path.expanduser('~')
CONFIG = os.path.join(HOME, '.config/budg/budget.ini')
AMOUNT = float(sys.argv[1])

# parse config
config = configparser.ConfigParser()
# if config file already exists
if os.path.isfile(CONFIG):

    # then load the file
    config.read(CONFIG)

# if config file does not exist
else:

    # create default config
    config['Necessities'] = {'Total': '50'}
    config['Savings'] = {'Total': '20'}
    config['Discretionary'] = {'Total': '30'}

    # save in default location
    with open(CONFIG, 'w') as configfile:
        config.write(configfile)

# go through categories in config
for section in config.sections():
    print(section)
    for category in config[section]:
        # calculate and show budget for category
        val = float(config[section][category]) * AMOUNT / 102
        txt = "  {}        ${:.2f}"
        print(txt.format(category, val))
