
def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    character_count = {}
    for char in text:
        char = char.lower()
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def char_dict(character_count):
    char_list = []
    for key, value in character_count.items():
        char_list.append({"char": key, "num": value})
    def sort_on(items):
        return items["num"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list

        