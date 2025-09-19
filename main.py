from stats import count_words, count_letters, sort_letters
import sys


def get_book_text(filename):
    with open(filename) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_file = sys.argv[1]
    book_text = get_book_text(book_file)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    character_counts = sort_letters(count_letters(book_text))
    for character in character_counts:
        if character["char"].isalpha():
            print(f"{character['char']}: {character['num']}")
    print("============= END ===============")


main()
