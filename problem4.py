import os

# Set the path of the directory you want to list
directory_path = '/users' \
''  # '.' means current directory

# Use os.listdir() to get list of files and directories
try:
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
