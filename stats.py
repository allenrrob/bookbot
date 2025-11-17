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
    return character_dict

def create_book_report(filepath):
    character_dict = character_count(filepath)
    new_character_dict = [{"char": k, "num": v} for k, v in character_dict.items() if k.isalpha()]
    new_character_dict.sort(key=lambda x: x["num"], reverse=True)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    count_words(filepath)
    print("--------- Character Count -------")
    for entry in new_character_dict:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")








