#!/bin/bash

#git fetch origin

function diff_files () {
    git diff origin/master --name-only
}

function build_commited () {
    # Build only commited changed
    #TODO: mode=sync/async
    git diff origin/master --name-only | xargs python3 stats.py --build --files
}

function build_all () {
    opt="$1"
    mode="$2" # sync/async
    if [ "$opt" = "--master-only" ] || [ "$opt" = "-m" ]; then
        git checkout master
        python3 stats.py --build --all
    elif [ "$opt" = "--master-with-commited"] || [ "$opt" = "-mc" ]; then
        python3 stats.py --build --all
    fi
}

cmd="$1"
mode="$2" # sync/async
opt="$3"
if [ "$cmd" = "--commited-only" ] || [ "$cmd" = "-c" ]; then
    build_commited
elif [ "$cmd" = "--all" ] || [ "$cmd" = "-a" ]; then
    build_all $opt
fi

exit 1
