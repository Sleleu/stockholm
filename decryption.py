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

def get_fernet(key_file)-> Fernet:
    try:
        with open(key_file, "rb") as file:
            decryption_key: bytes = file.read()
            fernet = Fernet(decryption_key)    
    except (OSError, ValueError) as error:
        print(error)
        exit(1)
    return fernet

def decrypt_file(fernet: Fernet, filepath: str)-> None:
    try:
        with open(filepath, "rb") as file:
            file_content = file.read()
    except OSError as error:
        print(error)
        return
    print(f"Decryption of {filepath} ...", end="")
    decrypted_content = fernet.decrypt(file_content)
    try:
        with open(filepath, "wb") as file:
            file.write(decrypted_content)
    except OSError as error:
        print(error)
        return
    print("| SUCCESS")

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
            print("file to decrypt :", filename)
            decrypt_file(fernet, filepath)
            os.rename(filepath, filepath[:-3])
            print(f"decrypted file: {filepath}")

    