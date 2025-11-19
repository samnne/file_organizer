import sys
import shutil
import os


def sort_files_directory(directory: str, sort_key_word: str = "") -> None:
    """
    Sort files given the directory to search for
    Args: directory: str => the directory you plan to organize,
          sort_key_word: str => the keyword in the file name you plan to sort
    Returns None
    """
    if directory[len(directory) - 1] != "/":
        directory += "/"

    dir_list: list[str] = os.listdir(directory)

    file_path: str = f"{directory}"

    for file in dir_list:
        cur_path: str = file_path + file
        root, ext = os.path.splitext(cur_path)
        if len(sort_key_word) > 1:
            ext: str = sort_key_word

        new_dir: str = file_path + ext[1 : len(ext)]
        if not os.path.isdir(new_dir):
            os.mkdir(new_dir)
            shutil.move(cur_path, f"{new_dir}")
        elif len(ext.split(".")) > 1 and ext[1 : len(file)] in file.lower():
            shutil.move(cur_path, f"{new_dir}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise Exception("Fail")

    dir: str
    key_word: str
    _, dir, key_word = sys.argv

    print(f"Sorting Files in {dir} by key word {key_word}")

    sort_files_directory(dir, key_word)
