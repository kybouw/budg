#! /bin/bash

################################################################################
# Budg - my python script for budgeting my paychecks
#
# Copyright (C) 2020  Kyle Bouwman
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
################################################################################


### variables

INSTALL_F_NP='The files needed to install are not in current working dir'

CONFIGLOC=$HOME/.config/budg
USERBINLOC=$HOME/bin

MAINSCRIPT=budg.py
DEFAULTCONF=defaultbudget.ini


### functions

# verify that the files needed exist in the current dir
verify_files() {

    echo "Verifying files..."

    local FILES_EXIST=true

    if [ ! -f "$MAINSCRIPT" ]; then
        FILES_EXIST=false
    fi
    if [ ! -f "$DEFAULTCONF" ]; then
        FILES_EXIST=false
    fi

    if [ "$FILES_EXIST" = false ]; then
        echo "$INSTALL_F_NP"
        exit 1
    fi

    echo "Files verified."
}

# verify that the neccessary dirs exist, or create them
create_dirs() {

    echo "Creating neccessary directories on your system..."

    # create ~/.config/budg
    if [ ! -d "$CONFIGLOC" ]; then
        mkdir -p "$CONFIGLOC"
    fi

    # create ~/bin
    if [ ! -d "$USERBINLOC" ]; then
        mkdir -p "$USERBINLOC"
    fi

    echo "Directories created."

}

copy_script() {

    echo "Copying script to user's home bin..."

    local BINFILE="$USERBINLOC"/budg
    cp "$MAINSCRIPT" "$BINFILE"
    chmod u+x "$BINFILE"

    echo "Script copied."

}

copy_config() {

    echo "Checking config..."

    if [ ! -f "$CONFIGLOC"/defaultbudget.ini ]; then
        cp "$DEFAULTCONF" "$CONFIGLOC"/defaultbudget.ini
    fi

    echo "Config created."
}

add_to_path() {

    echo "You must make sure your PATH includes ~/bin"
}

main() {

    echo "Starting install..."
    verify_files
    create_dirs
    copy_script
    copy_config
    echo "Install complete."
}

main


