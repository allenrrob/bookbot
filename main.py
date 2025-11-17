import sys

# import functions from stats.py
from stats import count_words
from stats import character_count
from stats import create_book_report


# Check for correct number of command-line arguments
if len(sys.argv) != 2:
     print("Usage: python3 main.py <path_to_book>")
     sys.exit(1)

# Get the filepath from command-line arguments
book_path = sys.argv[1]
     
# Create book report from book_path
def main():
     create_book_report(book_path)

main()

