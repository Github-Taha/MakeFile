#=================================================
# ---------------- Update Manager ----------------
#
# Taha Amir
# Monday, May 26, 2025
#
# Check for Updates
#=================================================

# Imports
import os
import sys

# Import Current Version File
import version

print("Checking for Updates...")
url = version.GIT_URL
save_path = 'version2.py'

try:
    urllib.request.urlretrieve(url, save_path)
    print("File found.")
except Exception as e:
    print(f"Failed to download file: {e}")

# Add the custom module's directory to sys.path
version2_module_path = r".\\"
if version2_module_path not in sys.path:
    sys.path.insert(0, version2_module_path)

# Import New Version File
import version2

if version2.VERSION != version.VERSION:
    print("New Version Available.")
else:
    print("You are on the latest Version.")

