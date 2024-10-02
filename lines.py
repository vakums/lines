import argparse
import chardet

def main():
    verbose_mode = False
    # setup argparse
    parser = argparse.ArgumentParser(description="Lines is a basic python script that display stats about a python file. For example, how many lines, characters, letters and digits are occurring in a given file.")
    parser.add_argument('-f', '--file', nargs="?", type=str, help="file path")
    args = parser.parse_args()

    if args.file:
        file_path = args.file
        if file_list:= get_file(file_path):
            file_stats(file_list)
    else:
        parser.error("No file specified")

def file_stats(file_list):
    characters = []
    letters = []
    digits = []
    whitespace = []
    others = []
    for line in file_list:
        for char in line:
            characters.append(char)
            if char.isalpha():
                letters.append(char)
            elif char.isdigit():
                digits.append(char)
            elif char.isspace():
                whitespace.append(char)
            else:
                others.append(char)

    print("characters:".title(), len(characters))
    print("letters:".title(), len(letters))
    print("digits:".title(), len(digits))
    print("whitespace:".title(), len(whitespace))
    print("symbols:".title(), len(others))

def get_file(file_path):
    try:
        with open(file_path, "rb") as f:
            file_data = f.read()
        detector = chardet.detect(file_data)
        encoding = detector["encoding"]
        file_list = file_data.decode(encoding).splitlines(keepends=True)
        return file_list
    except (FileNotFoundError, UnicodeDecodeError) as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    main()