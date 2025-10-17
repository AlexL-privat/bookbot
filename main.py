from pathlib import Path
from stats import count_words, sort_character_counts
import sys

def get_book_text(path):
    with open(path) as file:
        return file.read()
    

def print_report(book, num_words, sorted_unique_characters_count):
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {book}...")
    print ("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print ("--------- Character Count -------")
    for character in sorted_unique_characters_count:
        if character.isalpha() == True:
            print (f"{character}: {sorted_unique_characters_count[character]}")
    print ("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    book_path = Path(__file__).parent/book
    text = get_book_text(book_path)
    num_words = count_words(text)
    sorted_unique_characters_count = sort_character_counts(text)
    print_report(book, num_words, sorted_unique_characters_count)

main()