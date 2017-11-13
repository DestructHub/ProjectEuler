#!/bin/bash


function diff_files () {
    # Return uncommited changes file names
    git diff origin/master --name-only
}

function staged_files () {
    # Return staged file names
    git diff --cached --name-only
}

function build_uncommited () {
    # Build only commited changed
    diff_files | xargs python3 stats.py --build --files
}

function build_staged () {
    staged_files | xargs python3 stats.py --build --files
}

status=0

mode=$1
target=$2

if [ "$mode" = "" ]; then
    build_uncommited
elif [ "$mode" = "async" ]; then
    #TODO: stats.exs --build --files
    echo "Not Implemented"
    status=1
elif [ "$mode" = "sync" ]; then
    if [ "$target" = "diff" ]; then
        build_uncommited
    elif [ "$target" = "staged" ]; then
        build_staged
    fi
else
    echo "Usage : test.sh [sync|async] [diff|staged]"
    status=1
fi


exit $status
