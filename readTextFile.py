#!/usr/bin/env python3

"readTextFile -- Read a Text file"

# get file's name
fname = input("Input the file\'s name:")

# attemp to open the file for reading
try:
    fobj = open(fname, 'r')
except IOError as e:
    print("*** file open error:", e)
else:
    # display contents to the screen
    for eachLine in fobj:
        print(eachLine)
    fobj.close()
