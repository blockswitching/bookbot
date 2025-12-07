import sys
from stats import get_num_words, count_characters, sort_characters

# Reads the entire book text from the given file path
def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    # First command-line argument should be the path to the book file
    book_path = sys.argv[1]

    # Load the text from the file
    text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")

    # Count total words using helper function from stats.py
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")

    # Count characters and then sort them by frequency
    count = count_characters(text)
    sorted_chars = sort_characters(count)

    # Loop over sorted characters and print only alphabetic ones
    for item in sorted_chars:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():  # Only letters, skip punctuation and digits
            print(f"{ch}: {num}")

    print("============= END ===============")

# Ensure exactly one argument is passed (the book path)
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Start the program
main()
