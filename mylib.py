# =========================================================
# ------------------------ My Lib -------------------------
# =========================================================

# Imports
import os.path

# Show Title
def showTitle(title, clearScreen = True, width = 0):
    """
    Show Title
        Prints 45 new lines before printing the title
        underlined to the screen.

    Arguments:
        title: The title text to display
        width (optional): If you want the text centered,
            enter a value for width greater than the
            length of the title
            
    """

    if clearScreen:
        print("\n" * 45)
    if width <= 0:
        print(title)
        print("=" * len(title))
    else:
        print(("{:^" + str(width) + "}").format(title))
        print(("{:^" + str(width) + "}").format("=" * len(title)))

# Get File Name
def getFileName():
    """
    Get File Name
        Asks the user for a file name and
        checks if the file exists

    Returns:
        Returns the valid filename
    """

    while True:
        filename = input("Enter Filename: ")

        if os.path.exists(filename):
            break

        print("File does not exist. Please enter a valid filename.")

    return filename

# Center Text
def centerText(text, width):
    """
    Center Text
        Centers text by the width

    Arguments:
        text: Text to center
        width: The width value to center the text to
        
    """

    print(("{:^" + str(width) + "}").format(text))

# Get Valid Value
def validVal(pmt, err, a, b):
    """
    Valid Value
        Asks the user to enter an integer within the
        range of a and b, then returns that value back.

    Arguments:
        pmt: The Prompt for the user
        err: The Error message to display if the user
            does not enter a valid value
        a: The minimum value
        b: The maximum value

    Returns:
        Returns the valid integer entered by the user
    """
    
    while True:
        numInput = getInt(pmt, err)
        if numInput >= a and numInput <= b:
            break
        print(err)
    return numInput

# Get Valid Float
def validFloat(pmt, err, a, b):
    """
    Valid Float
        Asks the user to enter a float within the
        range of a and b, then returns that value back.

    Arguments:
        pmt: The Prompt for the user
        err: The Error message to display if the user
            does not enter a valid value
        a: The minimum value
        b: The maximum value

    Returns:
        Returns the valid float entered by the user
    """
    
    while True:
        numInput = getFloat(pmt, err)
        if numInput >= a and numInput <= b:
            break
        print(err)
    return numInput

# Valid Integer Measurment
def validMeasInt (pmt, err):
    """
    Valid Integer Measurment
        Asks the user to enter an integer greater
        than one.

    Arguments:
        pmt: The Prompt for the user
        err: The Error message to display if the user
        does not enter a valid value

    Returns:
        Returns the valid integer entered by the user
    """

    while True:
        numInput = getInt(pmt, err)
        if numInput >= 0:
            break
        print(err)
    return numInput

# Valid Float Measurment
def validMeasFloat (pmt, err):
    """
    Valid Float Measurment
        Asks the user to enter an float greater
        than one.

    Arguments:
        pmt: The Prompt for the user
        err: The Error message to display if the user
        does not enter a valid value

    Returns:
        Returns the valid float entered by the user
    """

    while True:
        numInput = getFloat(pmt, err)
        if numInput >= 0:
            break
        print(err)
    return numInput


# Get Yes or No
def getYorN(prompt, errTab = ""):
    """
    Get Yes or No
        Ask the user for either a yes or no answer,
        then returns the answer.

    Argument:
        prompt: The prompt for the user

    Returns:
        Returns the answer that the user has entered
    """
    
    while True:
        yorn = input(prompt).lower()
        if yorn == "y" or yorn == "n":
            break
        print(errTab + "You must enter y or n for yes or no.")
    return yorn

# Get Integer
def getInt(pmt, err):
    """
    Get Integer
        Ask the user for an integer, then return
        the value back.

    Arguments:
        pmt: The prompt for the user
        err: The error message to display if the user
            does not enter a valid value

    Returns:
        Returns the integer that was inputed
    """
    
    while True:
        try:
            numInput = int(input(pmt))
            break
        except ValueError:
            print(err)
    return numInput

# Get Float
def getFloat(pmt, err):
    """
    Get Float
        Ask the user for a float, then return
        the value back.

    Arguments:
        pmt: The prompt for the user
        err: The error message to display if the user
            does not enter a valid value

    Returns:
        Returns the float that was inputed
    """
    
    while True:
        try:
            numInput = float(input(pmt))
            break
        except ValueError:
            print(err)
    return numInput

# Enter to Continue
def pressEnter():
    """
    Press Enter
        Asks the user to press enter to continue.
    """
    
    input("Press [ENTER] to continue...")

