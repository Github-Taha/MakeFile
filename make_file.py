#=================================================
# ------------------- Make File ------------------
#
# Taha Amir
# Tuesday, May 13, 2025
#
# Make a new Python file with the neccessary
# options on it.
#=================================================

# Check for updates
import update_manager
import urllib.request
import os

def start_main():
    # Start the program
    if "version2.py" in os.listdir():
        os.remove("version2.py")
    input("\n\nPress [Enter] to continue...")
    import main

if update_manager.update_needed:
    print("Updating...")

    success = True

    try:
        import version2
        # Load up all the files
        filePathInit = 'https://raw.githubusercontent.com/Github-Taha/MakeFile/main/'
        for files in version2.FILES:
            filePath = filePathInit + files

            url = filePath
            save_path = filePath

            try:
                urllib.request.urlretrieve(url, files)
                print(f"File {files} downloaded.")
            except Exception as e:
                print(f"Failed to download file: {e}")
                success = False

        # If Download Successful
        if success:
            print("\n")
            print("Update Completed Successfully!")

            start_main()

        else:
            print("\n")
            print("Update could not complete.")
    except AttributeError:
        print("Programming Error. Starting program.")

        start_main()
else:
    start_main()
