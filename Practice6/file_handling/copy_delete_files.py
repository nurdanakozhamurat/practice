import shutil
import os

shutil.copy("python.txt", "newfile.txt")
print("Copied!")

if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
    print("Deleted!")