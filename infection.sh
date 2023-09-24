#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m' 

create_files() {
    echo "This is a simple file" > file.txt
    echo "Another simple file but with a .ft extension" > look.ft
    echo "aaaa bbbb cccc dddd this is the alphabet" > file2.txt
    echo "What a nice extension file !" > text.cub
    echo "I don't have any extension" > alone
    echo "int main(){return 0;}" > program.c
    git clone https://github.com/Sleleu/ft_transcendence.git

    mkdir sub_folder && cd sub_folder
    echo "Welcome to level 2" > level2.txt

    echo -e "Files sucessfully created in '${GREEN}$HOME/infection/${NC}' !"
    exit 0
}

delete_files() {
    rm -rfd "$HOME/infection"
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
        if [ $? -eq 0 ]; then
            echo "Infection folder created."
        else
            echo "Failed to create infection folder"
            exit 1
        fi
        cd "$HOME/infection"
        create_files
    fi
}
main "$1"