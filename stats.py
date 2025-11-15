def get_book_text(filepath):
    # Returns the contents of a file as a string
    with open(filepath) as f:
        return f.read()
    
def count_words(filepath):
     book_as_string = get_book_text(filepath)
     word_list = book_as_string.split()
     word_count = len(word_list)
          
     print(f"Found {word_count} total words")

def character_count(filepath):
    character_dict = {}
    book_as_string = get_book_text(filepath)
    for char in book_as_string:
        lower_char = char.lower()
        if lower_char not in character_dict:
            character_dict[lower_char]=1
        else:
            character_dict[lower_char] += 1


    print(character_dict)