#! /bin/bash

################################################################################
# Budg
# install.sh
# by Kyle Bouwman
# subject to MIT License (see LICENSE)
#
# Install script for the Budg python program
################################################################################


### variables

INSTALL_F_NP='The files needed to install are not in current working dir'

CONFIGLOC=$HOME/.config/budg
SCRIPTSLOC=$HOME/scripts/budg
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

    if [ ! -d "$CONFIGLOC" ]; then
        mkdir -p "$CONFIGLOC"
    fi
    if [ ! -d "$SCRIPTSLOC" ]; then
        mkdir -p "$SCRIPTSLOC"
    fi
    if [ ! -d "$USERBINLOC" ]; then
        mkdir -p "$USERBINLOC"
    fi

    echo "Directories created."

}

copy_script() {

    echo "Copying $MAINSCRIPT to $SCRIPTSLOC..."

    cp "$MAINSCRIPT" "$SCRIPTSLOC"

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

create_launcher() {

    echo "Creating launcher..."

    echo '#! /bin/bash' > "$USERBINLOC"/budg
    echo "" >> "$USERBINLOC"/budg
    echo 'python3 "$HOME"/scripts/budg/budg.py $1' >> "$USERBINLOC"/budg
    chmod u+x "$USERBINLOC"/budg

    add_to_path

    echo "Launcher created."
}

main() {

    echo "Starting install..."
    verify_files
    create_dirs
    copy_script
    copy_config
    create_launcher
    echo "Install complete."
}

main


