import shutil
import os

os.makedirs("another")

if os.path.exists("sample.txt"):
    shutil.move("sample.txt", "another/sample.txt")
    print("Moved")