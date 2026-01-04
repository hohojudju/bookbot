import sys

from stats import *


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    try:
        path_to_book = sys.argv[1]
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print("----------- Word Count ----------")
    word_count = count_words(get_book_text(path_to_book))
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    character_count = (count_characters(get_book_text(path_to_book)))
    sorted = count_sorted(character_count)

    for item in sorted:
        if item["char"].isalpha():
            print(item["char"] + ": " + str(item["num"]))

main()
