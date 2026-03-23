def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def main(filepath):
    text = get_book_text(filepath)
    word_count = get_word_count(text)
    print(f"Found {word_count} total words")

main("books/frankenstein.txt")
