from stats import get_word_count, get_character_count, char_dict

def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()

def main(filepath):
    text = get_book_text(filepath)
    word_count = get_word_count(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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

main("books/frankenstein.txt")