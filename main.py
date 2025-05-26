#=================================================
# ------------------- Make File ------------------
#
# Taha Amir
# Tuesday, May 13, 2025
#
# Make a new file
#=================================================

# Import Libraries
import subprocess
import sys
import os
import datetime
import re
import urllib.request

# Import Custom Libraries
import version
import mylib

# Check for updates
import update_manager
mylib.pressEnter()

print("\n" * 30)

# Initialization
filePath = "../"
date = datetime.datetime.now()
defaultName = version.DEFAULT_NAME
tab = version.TAB

# Intro
mylib.showTitle("File Initializer v4.0", False, 50)
print()

# Unit
unit = mylib.validVal("Enter Unit: ", "You must enter a value from 1 to 8.", 1, 8)
print()

filePath += version.UNIT + str(unit)

# Assignment or Practice Programs
print("Where do you want to put it? \n")
print("\t[1] Assignment")
print("\t[2] Practice Programs")
print("\t[3] Main")
print("\t[4] Custom")
print()

place = mylib.validVal("> ", "You must enter a valud from 1 to 4.", 1, 4)
print()

# Update FilePath
if place == 1:
    filePath += "/" + version.ASSIGNMENT
elif place == 2:
    ppn = mylib.validVal("Enter Practice Program Number: ", "You must enter a number.", 1, 10)

    filePath += "/" + version.PRACTICE_PROGRAMS + str(ppn)
elif place == 3:
    pass
elif place == 4:
    while True:
        custom = input("Enter custom Folder Name: ")
        if len(custom) > 0:
            break
        print("You must enter valid folder name.")
    filePath += "/" + custom

# Ask for FileName
while True:
    filenameD = input("Enter File Name: ")
    if len(filenameD) > 0:
        break
    print("You must enter a valid file name.")

# Ask for File Title
fileTitle = input("Enter File Title: ")
if fileTitle == "":
    fileTitle = filenameD

# Ask for Name
name = input("Enter Developer Name: ")
if name == "":
    name = defaultName

# Ask for Description
print("Enter Description:\n")
descrip = []
while True:
    line = input("\t")
    if line == "":
        break
    descrip.append(line)

# Make FileName
filename = "".join(filenameD.split(" "))
if not filename.endswith(".py"):
    filename += ".py"

# Update FilePath
filePath += "/" + filename

# Check if the file exists
if os.path.exists(filePath) and mylib.getYorN("\nFile Exists.\nDo you want to overwrite (y/n)? ") == "n":
    print("Canceling File Creation.")

    mylib.pressEnter()
else:
    print()

    # Creating Directories
    print("Making directories...")
    os.makedirs(os.path.dirname(filePath), exist_ok=True)

    imports = []

    # Asking for Imports
    if mylib.getYorN("Do you want to add imports? ") == "y":
        while True:
            imp = input("\tImport: ")
            if imp == "":
                break
            imports.append(imp)
                    
    functions = []

    # Asking for Functions
    functions = []
    if mylib.getYorN("Do you want add functions? ") == "y":
        while True:
            print()

            end = False
            # Function Name
            while True:
                funcName = input("\tFunction Name: ")
                if funcName == "":
                    end = True
                    break
                if re.search("^[a-zA-Z_][a-zA-Z0-9_]+$", funcName):
                    break
                print("\tEnter valid Function Name.")
            print()

            # End if Function Name Empty
            if end:
                break

            # Function Description
            print("\tEnter Function Description:")
            funcDescrip = []
            while True:
                line = input("\t\t")
                if line == "":
                    break
                funcDescrip.append(line)

            params = []
            if mylib.getYorN("\tDo you want to add Parameters? ", "\t") == "y":
                # Parameters
                while True:
                    end = False
                    # Get Param
                    while True:
                        paramName = input("\t\tParameter Name: ")
                        if paramName == "":
                            end = True
                            break
                        if re.search("^[a-zA-Z_][a-zA-Z0-9_]+$", paramName):
                            break
                        print("\t\tPlease Enter Valid Parameter.")

                    # If End, Break out of Param Loop
                    if end:
                        break

                    # Parameter Description
                    print("\t\tEnter Parameter Description:")
                    paramDescrip = []
                    while True:
                        line = input("\t\t\t")
                        if line == "":
                            break
                        paramDescrip.append(line)

                    params.append({
                        "name": paramName,
                        "descrip": paramDescrip
                    })

            print()
            
            # Return
            ret = {
                "name": "",
                "descrip": []
            }
            if mylib.getYorN("\tDo you want to add a return value? ", "\t") == "y":
                # Return Name
                while True:
                    retVar = input("\t\tEnter Return Value Name: ")
                    if re.search("^[a-zA-Z_][a-zA-Z0-9_]+$", retVar):
                        break
                    print("\t\tPlease Enter valid return value name.")

                # Return Description
                print("\t\tEnter Parameter Description:")
                retDescrip = []
                while True:
                    line = input("\t\t\t")
                    if line == "":
                        break
                    retDescrip.append(line)

                # Return Value
                ret = {
                    "name": retVar,
                    "descrip": retDescrip
                }
                    
            """
            Functions
            {
                Name: FunctionName
                Descrip: FunctionDescription
                Params:
                    [
                        {
                            Name: ParamName
                            Descrip: ParamDescription
                        }
                    ]
                Return:
                {
                    Name: RetName
                    Descrip: RetDescription
                }
            }
            """

            functions.append(
                {
                    "name": funcName,
                    "descrip": funcDescrip,
                    "params": params,
                    "return": ret
                }
            )

    print(functions)

    # Opening File
    print("Writing to file...")
    pyFile = open(filePath, "w")

    # Writing Data to file

    # Write Header
    pyFile.write("#" + "=" * 49 + "\n")
    pyFile.write("#" + "{:-^48}\n".format(" " + fileTitle + " "))
    pyFile.write("#\n")
    pyFile.write("# {}\n".format(name))
    pyFile.write("# {}, {} {}, {}\n".format(date.strftime("%A"), date.strftime("%B"), date.day, date.year))
    pyFile.write("#\n")
    for l in descrip:
        pyFile.write("# {}\n".format(l))
    pyFile.write("#" + "=" * 49 + "\n")
    pyFile.write("\n\n")

    # Write Imports
    pyFile.write("# Imports\n")
    for imp in imports:
        pyFile.write("import " + imp + "\n")
    pyFile.write("\n\n")

    # Write Functions
    pyFile.write("# Functions\n\n")
    for func in functions:
        # Define Line
        firstLine = "def " + func["name"] + "("
        if len(func["params"]) > 0:
            for param in func["params"]:
                firstLine += param["name"] + ", "
            firstLine = firstLine[:-2]

        firstLine += "):\n"
        pyFile.write(firstLine)

        # DocString
        pyFile.write(tab + '"""\n')

        # Function Description
        for descripLine in func["descrip"]:
            pyFile.write(tab * 2 + descripLine + "\n")
        pyFile.write("\n")

        # Parameters
        if len(func["params"]) > 0:
            pyFile.write(tab + "Arguments:\n")
            for param in func["params"]:
                pyFile.write(tab * 2 + param["name"] + ":\n")
                for paramDescrip in param["descrip"]:
                    pyFile.write(tab * 3 + paramDescrip + "\n")
        pyFile.write("\n")

        # Return
        if func["return"]["name"] != "":
            pyFile.write(tab + "Return:\n")
            pyFile.write(tab * 2 + func["return"]["name"] + ":\n")
            for retDescrip in func["return"]["descrip"]:
                pyFile.write(tab * 3 + retDescrip + "\n")

        pyFile.write(tab + '"""\n')
        pyFile.write(tab + "\n")
        pyFile.write(tab + "pass\n\n")
            
    
    pyFile.write("\n\n")

    # Write Main
    pyFile.write("# ====== Main ======\n\n\n\n")
    pyFile.write("input('Press [Enter] to exit... ')")

    pyFile.close()

    # Opening File in IDLE
    print("Opening File...")
    # Full path to your file
    full_filePath = os.path.abspath(filePath)
    # Use the same Python executable running this script to open IDLE
    subprocess.Popen([sys.executable, "-m", "idlelib", full_filePath])

    mylib.pressEnter()


print("Exiting Program.")

mylib.pressEnter()
