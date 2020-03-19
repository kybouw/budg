#! /usr/bin/python3

################################################################################
# budg - my python script for budgeting my paychecks
#
# Copyright (C) 2020 Kyle Bouwman
#
# This file is part of budg.
#
# budg is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# budg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with budg.  If not, see <https://www.gnu.org/licenses/gpl.html>.
################################################################################

# imports
import configparser
import os.path
import sys

# function that handles input errors
def usage_error():
    print('Usage: budget XXX.XX')
    print('Invalid argument')
    exit(1)
    
# verify args
if len(sys.argv) != 2:
    usage_error()

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
