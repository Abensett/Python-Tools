# sys is a module used to get the arguments passed to the script 
# when it is executed from the command line
import sys
import os

if len(sys.argv) < 2:
    print("Please provide the name of the file as the first arg !")
    sys.exit()

arg = sys.argv[1]
print(arg, "is about to be opened and processed ...")

# try to open the file in read mode
try:
    file = open(arg, "r")
# if the file does not exist or could not be opened
# IOError = input/output error (file not found or permission denied)
except IOError as error:
    print("The file does not exist or could not be opened : ", error)
    exit(1)
    
# readlines returns a list of the lines in the file
ContentFile = file.readlines()
file.close()

# find the longest line
LongestLine = 0
for line in ContentFile:
    if len(line) > LongestLine:
        LongestLine = len(line)

MakefileHeader = "header:\n"
ListChar = ["\"","\'","`"]
# add printf and " ", add \n at the end of each line and \ before " ' `
for line in ContentFile:
    line = line.replace("\'", "\\\'")
    line = line.replace("\"", "\\\"")
    line = line.replace("`", "\`")
    LineToAdd = "\t@printf \" " + line[:len(line)-1:] + "\\n\" "
    MakefileHeader += LineToAdd + "\n"

# create a fold Heardes if it does not exist
try:
    os.mkdir("Headers")
except FileExistsError:
    print("The file is about to be created in Headers/ .")

# check if the file already exists
try:
    MakefileHeaderFile = open("Headers/MakefileHeader" + arg, "w")
except IOError as e:
    print("The file could not be created : ", e)

MakefileHeaderFile.write(MakefileHeader)
MakefileHeaderFile.close()

print("MakefileHeader" + arg, "containing your header has been created !")