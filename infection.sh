#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m' 

create_files() {
    echo "This is a simple file" > file.txt
    echo "Another simple file but with a .ft extension" > file2.txt.ft
    echo "aaaa bbbb cccc dddd this is the alphabet" > file2.txt
    echo "What a nice extension file !" > text.cub

    echo -e "Files sucessfully created in '${GREEN}$HOME/infection/${NC}' !"
    exit 0
}

delete_files() {
    rm -rd "$HOME/infection"
    echo "Infection folder sucessfully deleted !"
    exit 0
}

main() {
    # check env var
    if [ -z "$HOME" ]; then
        echo "Did you unset HOME smarty-pants? :)"
        exit 1
    fi
    if [ "$1" == "delete" ]; then
        delete_files
    fi
    # check if infection folder exist
    if [ -d "$HOME/infection" ]; then
        echo "Infection folder already exist."
        exit 1
    else
        # create infection folder in home
        mkdir "$HOME/infection"
        echo "Infection folder created."
        cd "$HOME/infection"
        create_files
    fi
}
main "$1"