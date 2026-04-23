# Listing Files and Directories in Python using os Module
import os
#specify the directory you want to list
directory_path = '/'
#List all the files and directories in the specified path
contents = os.listdir(directory_path)
#Print each file and directory name
for item in contents:
    print(item)