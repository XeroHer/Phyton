import os
# os.remove("dsti.txt")

if os.path.exists("dsti.txt"):
    os.remove("dsti.txt")
else:
    print("The file is not exist")


# Delete Folder
os.rmdir("myFolder")