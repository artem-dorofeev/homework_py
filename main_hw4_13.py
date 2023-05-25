from pathlib import Path


def parse_folder(path):
    files = []
    folders = []

    for i in path.iterdir():
        if i.is_dir():
            folders.append(i.name)
        else:
            files.append(i.name)

    return files, folders


p = Path('/home/A.Dorofeev/Desktop/test/')

result = parse_folder(p)
print(result)
