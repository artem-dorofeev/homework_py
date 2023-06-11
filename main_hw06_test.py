import sys
from pathlib import Path
import uuid

from main_hw06_normalize import normalize


CATEGORIES = {"Audio": [".mp3", ".aiff"],
              "Documents": [".docx", ".txt", ".pdf", ".doc", ".xlsx", ".xls"],
              "Photo": [".jpg", ".raw", ".nef"],
              "Video": [".avi", ".mp4", ".mkv"]}

list_folder = ("Audio", "Documents", "Photo", "Video")


def move_file(file: Path, root_dir: Path, categorie: str) -> None:
    target_dir = root_dir.joinpath(categorie)
    if not target_dir.exists():
        # print(f"Make {target_dir}")
        target_dir.mkdir()
    # print(path.suffix)
    # print(target_dir.joinpath(f"{normalize(path.stem)}{path.suffix}"))
    new_name = target_dir.joinpath(f"{normalize(file.stem)}{file.suffix}")
    if new_name.exists():
        new_name = new_name.with_name(
            f"{new_name.stem}-{uuid.uuid4()}{file.suffix}")
    file.rename(new_name)


def get_categories(file: Path) -> str:
    ext = file.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat
    return "Other"


# # def show_all_files(path: Path) -> None:
# #     data = []
# #     for item in path.iterdir():
# #         if item.is_dir():
# #             data.extend(show_all_files(item))
# #         else:
# #             data.append(item)
# #     return data

# def show_all_files(path: Path) -> None:
#     for item in path.iterdir():
#         if item.is_dir():
#             show_all_files(item)
    #     continue
    # print(item)


def sort_folder(path: Path) -> None:

    for item in path.glob("**/*"):
        # print(item)

        if item.is_file():
            print(f'this is file {item}')
            # cat = get_categories(item)
            # move_file(item, path, cat)

    for item in path.glob("**/*"):
        if item.is_dir():
            # print(f'this is dir {item}')
            # print(item.name)

            if item.name not in list_folder:

                try:
                    item.rmdir()
                except OSError:
                    continue


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
