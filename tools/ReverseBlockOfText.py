# This program reverses the order of the words in a block of text.
# Considering the longest line as the width of the block

import sys
import os

if len(sys.argv) < 2:
    print("Please provide the name of the file as the first arg !")
    sys.exit()

Arg = sys.argv[1]

# try to open the file in read mode
try:
    ContentFile = open(Arg, "r")
except IOError as error :
    print("The file does not exist or could not be opened : ", error)
    exit(1)

ContentFileList = []
# find the longest line
LongestLine = 0
for line in ContentFile:
    ContentFileList.append(line)
    if len(line) > LongestLine:
        LongestLine = len(line)

ReversedContent = ""

for line in ContentFileList:
    line = line[:len(line)-1:]
    if (len(line) < LongestLine):
        line = line + " " * (LongestLine - len(line)) + "\n"
    ReversedContent += line[::-1]

# create a fold Reversed if it does not exist
try:
    os.mkdir("Reversed")
except FileExistsError as error:
    print("The file is about to be created in Reversed/")

# check if the file already exists
try:
    ReversedContentFile = open("Reversed/Reversed" + Arg, "w")  
except IOError as error:
    print("The file could not be created : ,", error)

ReversedContentFile.write(ReversedContent)
ReversedContentFile.close()

print("Reversed" + Arg, "containing your reversed text has been created !")