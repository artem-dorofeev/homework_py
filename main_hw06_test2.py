import sys
from pathlib import Path
# import uuid
import shutil

from main_hw06_normalize import normalize

count_files = 0

CATEGORIES = {"Audio": [".mp3", ".aiff", ".m3u"],
              "Documents": [".docx", ".txt", ".pdf", ".doc", ".xlsx", ".xls"],
              "Photo": [".jpg", ".raw", ".nef"],
              "Video": [".avi", ".mp4", ".mkv"],
              "Archives": [".zip", ".rar", ".tar", ".gz"]}

LIST_FOLDERS_SORT = ("Audio", "Documents", "Photo",
                     "Video", "Other", "Archives")


def move_file(file: Path, root_dir: Path, categorie: str) -> None:
    target_dir = root_dir.joinpath(categorie)
    if not target_dir.exists():
        target_dir.mkdir()
    new_name = target_dir.joinpath(f"{normalize(file.stem)}{file.suffix}")

    file.rename(new_name)


def get_categories(file: Path) -> str:
    ext = file.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            print(f'category for {file.stem}{file.suffix} is {cat}')
            return cat
    return "Other"


def sort_folder(path: Path) -> None:
    global count_files
    for item in path.glob("**/*"):
        # print(item)
        if item.is_file():
            # print(item.stem)
            count_files += 1
            cat = get_categories(item)
            move_file(item, path, cat)


def main():
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "No path to folder"

    if not path.exists():
        return f"Folder with path {path} dos`n exists."

    sort_folder(path)
    # delete_emppty_folders(path)
    # upack_archive(path)

    return "All ok"


if __name__ == "__main__":
    print(main())
    print(count_files)
