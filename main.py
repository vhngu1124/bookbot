from stats import get_num_words
from stats import count_letters
from stats import sort_on
from stats import dictionary_to_list
import sys

def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_contents = get_book_text()
    word_count = get_num_words(book_contents)
    letter_dictionary = count_letters(book_contents)
    sorted_dictionary = dictionary_to_list(letter_dictionary)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_dictionary:
        print(f"{entry['letter']}: {entry['count']}")
main()