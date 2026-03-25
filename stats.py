
def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    character_count = {

    }
    for char in text:
        char = char.lower()
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    print(character_count)

