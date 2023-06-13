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

LIST_FOLDERS_SORT = ("Audio", "Documents", "Photo",
                     "Video", "Other", "Archives")

count_file = 0
# count_file2 = 0
# count_file3 = 0
# count_archive = 0
# count_del_folder = 0


# def move_file(file: Path, root_dir: Path, categorie: str) -> None:
#     target_dir = root_dir.joinpath(categorie)
#     if not target_dir.exists():
#         target_dir.mkdir()
#     new_name = target_dir.joinpath(f"{normalize(file.stem)}{file.suffix}")
#     index = None
#     if new_name.exists():
#         index = len([f for f in target_dir.glob(
#             "*") if new_name.stem in f.stem])
#     new_name = new_name.with_name(
#         f"{new_name.stem}{index if index else ''}{file.suffix}")
#     file.rename(new_name)


# def get_categories(file: Path) -> str:

#     ext = file.suffix.lower()
#     for cat, exts in CATEGORIES.items():
#         if ext in exts:
#             return cat
#     return "Other"


# def sort_folder(path: Path) -> None:
#     for item in path.glob("*/"):
#         print(item)

def sort_folder(path: Path) -> None:
    global count_file
    # global LIST_FOLDERS_SORT
    objects_list = path.glob("*/")
    for item in [i for i in objects_list if i.name not in LIST_FOLDERS_SORT]:
        # print(f'count in for {count_file}')
        # print(item.stem)
        # if item.stem not in LIST_FOLDERS_SORT:
        print(item.stem)
        if item.is_file():
            print(f'count in if {count_file}')
            count_file += 1
            print(item)
            # cat = get_categories(item)
            # move_file(item, path, cat)
        else:
            print(item.stem, count_file)


# def sort_folder(path: Path) -> None:
#     global count_file
#     global LIST_FOLDERS_SORT
#     for item in path.glob("**/*"):
#         # print(f'count in for {count_file}')
#         # print(item.stem)
#         if item.stem not in LIST_FOLDERS_SORT:
#             print(item.stem)
#             if item.is_file():
#                 # print(f'count in if {count_file}')
#                 count_file += 1
#                 # print(item)
#                 cat = get_categories(item)
#                 move_file(item, path, cat)
#         else:
#             print(item.stem, count_file)


# def del_emppty_folders(path: Path) -> None:
#     global count_del_folder
#     global LIST_FOLDERS_SORT

#     for item in path.iterdir():
#         if item.name not in LIST_FOLDERS_SORT:

#             if item.is_dir():
#                 del_emppty_folders(item)
#                 try:
#                     item.rmdir()
#                     count_del_folder += 1
#                 except OSError:
#                     print(f'folder {item.name} is not emppty')
#                     continue

#             continue


# def upack_archive(path: Path) -> None:
#     global count_archive
#     arch_path = path.joinpath("Archives")
#     if arch_path.exists():

#         for item in arch_path.iterdir():
#             # print(f'archive - {item.stem}')
#             output_arch = arch_path.joinpath(item.stem)
#             # print(output_arch)
#             output_arch.mkdir()
#             shutil.unpack_archive(item, output_arch)
#             count_archive += 1


def main():
    global count_file
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "No path to folder"

    if not path.exists():
        return f"Folder with path {path} dos`n exists."

    sort_folder(path)
    print(f'summ files - {count_file}')
    # del_emppty_folders(path)
    # upack_archive(path)

    return "All ok"


if __name__ == "__main__":
    print(main())
    # print(
    #     f'Number of moved files - {count_file}\nNumber of unpack archive - {count_archive}\nNumber of delete folder - {count_del_folder}')
