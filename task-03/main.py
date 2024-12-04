import sys
from pathlib import Path
from colorama import Fore, Back, Style


def parse_folder(path):
    
    for element in path.iterdir():
        if element.is_dir():
            parse_folder(element)
            print(Fore.MAGENTA + f"Folder {element}")
        else:
            print(Fore.GREEN + f"file : {element}")
    
    print(Style.RESET_ALL)
    



if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage:  python3 main.py images")
        print("\tpython3 main.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    directory = Path(folder_path)

    if not directory.exists():
        print(Back.RED + "Entered folder not exist. Please enter folder as argument" + Style.RESET_ALL)
        sys.exit()
    
    if not directory.is_dir():
        print(Back.YELLOW + "Entered data is not a directory. Please enter directory name as argument" + Style.RESET_ALL)
        sys.exit()

    parse_folder(directory)