import pathlib    
path = pathlib.Path(r"TestFolder")
for root, dirs, files in path.walk():
    print("Root: ")
    print(root)
    print("Dirs: ")
    print(dirs)
    print("Files: ")
    print(files)
    print("")
