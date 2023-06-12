import sys
from pathlib import Path
# import uuid
import shutil

from main_hw06_normalize import normalize


CATEGORIES = {"Audio": [".mp3", ".aiff", ".m3u"],
              "Documents": [".docx", ".txt", ".pdf", ".doc", ".xlsx", ".xls"],
              "Photo": [".jpg", ".raw", ".nef"],
              "Video": [".avi", ".mp4", ".mkv"],
              "Archives": [".zip", ".rar", ".tar", ".gz"]}

list_folder = ("Audio", "Documents", "Photo", "Video", "Other", "Archives")


def move_file(file: Path, root_dir: Path, categorie: str) -> None:
    target_dir = root_dir.joinpath(categorie)
    if not target_dir.exists():
        target_dir.mkdir()
    new_name = target_dir.joinpath(f"{normalize(file.stem)}{file.suffix}")
    index = None
    if new_name.exists():
        index = len([f for f in target_dir.glob(
            "*") if new_name.stem in f.stem])
        print(new_name)
        print(index)
    # while True:
    #     if new_name.exists():
    # #         # print(f'name {file} == {new_name}')
    new_name = new_name.with_name(
        f"{new_name.stem}{index if index else ''}{file.suffix}")
    #     index += 1
    # else:
    file.rename(new_name)
    # break


# def move_file(file: Path, root_dir: Path, categorie: str) -> None:
#     target_dir = root_dir.joinpath(categorie)
#     if not target_dir.exists():
#         target_dir.mkdir()
#     new_name = target_dir.joinpath(f"{normalize(file.stem)}{file.suffix}")
#     index = 1
#     while True:

#         if new_name.exists():
#             # print(f'name {file} == {new_name}')
#             new_name = new_name.with_name(
#                 f"{new_name.stem}_{index}{file.suffix}")
#             index += 1
#         else:
#             file.rename(new_name)
#             break

    # file.rename(new_name)


def get_categories(file: Path) -> str:
    ext = file.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat
    return "Other"


def sort_folder(path: Path) -> None:

    for item in path.glob("**/*"):
        # print(item)

        if item.is_file():
            # print(f'this is file {item}')
            cat = get_categories(item)
            move_file(item, path, cat)


def del_emppty_folders(path: Path) -> None:
    for item in path.iterdir():
        if item.name not in list_folder:

            if item.is_dir():
                del_emppty_folders(item)
                try:
                    item.rmdir()
                except OSError:
                    print(f'folder {item.name} is not emppty')
                    continue

            continue


def upack_archive(path: Path) -> None:
    arch_path = path.joinpath("Archives")
    if arch_path.exists():

        for item in arch_path.iterdir():
            # print(f'archive - {item.stem}')
            output_arch = arch_path.joinpath(item.stem)
            # print(output_arch)
            output_arch.mkdir()
            shutil.unpack_archive(item, output_arch)


def main():
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "No path to folder"

    if not path.exists():
        return f"Folder with path {path} dos`n exists."

    sort_folder(path)
    del_emppty_folders(path)
    upack_archive(path)

    return "All ok"


if __name__ == "__main__":
    print(main())
