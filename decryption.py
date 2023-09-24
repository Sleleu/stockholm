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
    except OSError as error:
        print(error)
        exit(1)
    fernet = Fernet(decryption_key)
    return fernet

def decryption(key_file: str, path: str, silent: bool)-> None:
    fernet = get_fernet(key_file)
    files = os.listdir(path)
    for filename in files:
        filepath = os.path.join(path, filename)
        file_extension = "." + filepath.split(".")[-1]
        print(file_extension)
        if os.path.isdir(filepath) is True:
            decryption(key_file, filepath, silent)
        else:
            if file_extension not in wannacry_extensions:
                continue
            print(file_extension)

    