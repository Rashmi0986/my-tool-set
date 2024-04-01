import pathlib    
path = pathlib.Path(r"TestFolder")
for p in path.rglob("*"):
    print(p.name)
    # p.is_dir(), p.is_file()