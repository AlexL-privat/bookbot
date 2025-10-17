def count_words(text):
    words = text.split()
    result = len(words)
    return result

def count_unique_characters(text):
    character_counts = {}
    for character in text:
        character = character.lower()
        if character not in character_counts:
            character_counts[character] = 1
        else:
            character_counts[character] += 1
    return character_counts



def sort_character_counts(text):
    character_counts = count_unique_characters(text)
    return dict(sorted(character_counts.items(), key=lambda item: item[1], reverse=True))