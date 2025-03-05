import sys
from stats import count_words, count_chars, sort_chars

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Store text of supplied file
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

# Go to work
def main():
    book_path = sys.argv[1]
    word_count = count_words(get_book_text(book_path))
    char_count = count_chars(get_book_text(book_path))
    sorted_chars = sort_chars(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in range(len(sorted_chars)):
        print(f"{sorted_chars[i]["char"]}: {sorted_chars[i]["count"]}")
    print("============= END ===============")

main()