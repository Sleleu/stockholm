## About this project

Stockholm is a project aimed at testing and gaining a better understanding of how ransomware functions.
It encrypts data using the Fernet encryption method and appends the '.ft' extension to
all files within the specified folder.
This program exclusively operates within a folder named 'infection' located in the 
user's HOME directory and only encrypts files whose extensions have been targeted by
Wannacry.

**Disclaimer:** This project is for educational purposes only. You should never use this type of program for malicious purposes.

## Usage

In the first step, it is necessary to create a 'infection' directory within the user's HOME, either manually or by using `make` or `./infection.sh` command. Once the directory is created, simply run the script without any options to encrypt the files located within this directory:

```shell
./stockholm.py
```

At the same time, the script will store the encryption key in a `master.key`. file. This key can be used to decrypt the files as follows:

```shell
./stockholm.py --reverse master.key
```

Additionally, the following options are available: :

- `-h`, `--help`: display the help.
- `-v`, `--version`: show the version of the program.
- `-s`, `--silent`: the program will not produce any output.
