def get_book_text(filepath):
    # Returns the contents of a file as a string
    with open(filepath) as f:
        return f.read()
    
def count_words(filepath):
     book_as_string = get_book_text(filepath)
     word_list = book_as_string.split()
     word_count = len(word_list)
          
     print(f"Found {word_count} total words")
