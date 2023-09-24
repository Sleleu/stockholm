# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    decryption.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sleleu <sleleu@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/23 03:21:32 by sleleu            #+#    #+#              #
#    Updated: 2023/09/23 03:21:46 by sleleu           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
from cryptography.fernet import Fernet
from encryption import wannacry_extensions

LIGHT_GREEN = "\033[1;32m"
LIGHT_RED = "\033[1;31m"
YELLOW = "\033[1;33m"
LIGHT_CYAN = "\033[1;36m"
END = "\033[0m"

def get_fernet(key_file)-> Fernet:
    try:
        with open(key_file, "rb") as file:
            decryption_key: bytes = file.read()
            fernet = Fernet(decryption_key)    
    except (OSError, ValueError) as error:
        print(error)
        exit(1)
    return fernet

def decrypt_file(fernet: Fernet, filepath: str, silent: bool)-> None:
    try:
        with open(filepath, "rb") as file:
            file_content = file.read()
    except OSError as error:
        print(error)
        return
    if silent is False:
        print(f"{LIGHT_CYAN}Decryption of {YELLOW}'{filepath}'{LIGHT_CYAN} ...{END}", end="")
    try:
        decrypted_content = fernet.decrypt(file_content)
    except:
        print(f"{LIGHT_RED}| Failed to decrypt file: Invalid key{END}")
        return
    try:
        with open(filepath, "wb") as file:
            file.write(decrypted_content)
    except OSError as error:
        print(error)
        return
    if silent is False:
        print(f"{LIGHT_CYAN}| {LIGHT_GREEN}SUCCESS{END}")

def decryption(key_file: str, path: str, silent: bool)-> None:
    fernet = get_fernet(key_file)
    files = os.listdir(path)
    for filename in files:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath) is True:
            decryption(key_file, filepath, silent)        
        elif filepath.endswith(".ft") is False:
            continue
        else:
            old_filepath = filepath[:-3]
            old_filextension = "." + old_filepath.split(".")[-1]
            if old_filextension not in wannacry_extensions:
                continue
            decrypt_file(fernet, filepath, silent)
            os.rename(filepath, filepath[:-3])

    