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


# trouver dossier infection dans le HOME du user


# Les fichiers doivent être chiffres
# Les fichiers doivent être renommés en ajoutant .ft, sauf si ils ont déjà le .ft

# La clé doit faire au minimum 16 characteres

# Dechiffrement, possibilité de dechiffrer les fichiers avec la clé

if __name__ == "__main__":
    print("bang")