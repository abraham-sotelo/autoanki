#!/bin/bash

# Jump to my project dir and activate the venv
directory=$(dirname $(readlink -f $0))
cd $directory

project=$(basename $directory)
source ${HOME}/python/venvs/$project/bin/activate
