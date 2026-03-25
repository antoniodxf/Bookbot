from stats import get_word_count, get_character_count

def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()

def main(filepath):
    text = get_book_text(filepath)
    word_count = get_word_count(text)
    print(f"Found {word_count} total words")
    get_character_count(text)

main("books/frankenstein.txt")
