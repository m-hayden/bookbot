from stats import (
    get_word_count,
    get_char_count,
    sort_dict
)
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    book_text = get_book_text(filepath)
    print(f"Analyzing book found at {filepath}...")
    num_words = get_word_count(book_text)
    char_count = get_char_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    char_count_list = sort_dict(char_count)
    print("--------- Character Count -------")
    for key in char_count_list:
        print(f'{key["char"]}: {key["num"]}')
    print("============= END ===============")
        

main()