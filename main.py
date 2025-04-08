import sys # system arguments
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return(contents)

from stats import sort_char_count
from stats import word_count
from stats import character_count
    
def main():
    path = sys.argv[1] # relative path to user input
    text = get_book_text(path)
    num_words = word_count(text)
    char_count_dict = character_count(text)

    sorted_chars = sort_char_count(char_count_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()
