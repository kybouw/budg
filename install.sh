#! /bin/bash

################################################################################
# budg - my python script for budgeting my paychecks
#
# Copyright (C) 2022 Kyle Bouwman
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

## globals
EXE_DIR_LOCATION="${HOME}/.local/bin"
EXE_LOCATION="${EXE_DIR_LOCATION}/budg"
PLAN_DIR_LOCATION="${HOME}/.config/budg"
# dependencies
EXE_SRC_LOCATION="./budg/budg.py"
DEFAULTPLAN_SRC_LOCATION="./budg/defaultplan.ini"

## checks to make sure that source files are present where expected
#  return 1 if a file is missing
#  return 0 if both files are present
function verify_dependencies {
    echo "Verifying files are present..."

    # check exe exists
    if [ ! -f "${EXE_SRC_LOCATION}" ]; then
        echo "File \"${EXE_SRC_LOCATION}\" does not exist"
        return 1
    fi

    # check default plan exists
    if [ ! -f "${DEFAULTPLAN_SRC_LOCATION}" ]; then
        echo "File \"${DEFAULTPLAN_SRC_LOCATION}\" does not exist"
        return 1
    fi

    return 0
}

function create_dirs {
    echo "Creating install directories..."

    # create exe install location
    if [ ! -d "${EXE_DIR_LOCATION}" ]; then
        mkdir -p "${EXE_DIR_LOCATION}"
    fi

    # create plan install location
    if [ ! -d "${PLAN_DIR_LOCATION}" ]; then
        mkdir -p "${PLAN_DIR_LOCATION}"
    fi

}

function copy_files {
    echo "Copying files..."

    # copy exe to install location and make executable
    cp "${EXE_SRC_LOCATION}" "${EXE_LOCATION}"
    chmod u+x "${EXE_LOCATION}"
    
    # copy default plan to install location
    cp "${DEFAULTPLAN_SRC_LOCATION}" "${PLAN_DIR_LOCATION}"

}

function install_failure {
    echo "Install failed"
    exit
}

verify_dependencies || install_failure

create_dirs || install_failure

copy_files && echo "Install succeeded"