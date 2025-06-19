from stats import get_num_words, get_num_characters, sort_num_characters
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def print_report(num_words, book_path, sorted_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_characters:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    sorted_characters = sort_num_characters(num_characters)
    print_report(num_words, book_path, sorted_characters)

main() 
