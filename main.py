from stats import get_word_count, get_character_count, char_dict
import sys

def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()

def main(filepath):
    text = get_book_text(filepath)
    word_count = get_word_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    character_count = get_character_count(text)
    char_list = char_dict(character_count)
    for item in char_list:
        char = item['char']
        count = item['num']
        if char.isalpha():
            print(f'{char}: {count}')
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])