def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    # Convert all characters to lowercase
    text = text.lower()
    
    # Create an empty dictionary to store character counts
    counts = {}
    
    # Loop through each character in the text
    for char in text:
        # Check if we've seen this character before
        if char in counts:
            # If yes, increment its count
            counts[char] += 1
        else:
            # If no, add it to the dictionary with count 1
            counts[char] = 1
    
    # Return the completed dictionary
    return counts

def sort_char_count(char_dict):
    # first, a list to hold dictionaries
    chars_list = []
    # second, for each character and count in the input dictionary
    for char, count in char_dict.items():
        # create dictionary with 'char' and 'count' keys
        char_info = {"char": char, "count": count}
        # add the dictionary to the list
        chars_list.append(char_info)

    # define function to tell sort() what to use
    def sort_on(dict):
        return dict["count"]
    
    # sort list by count (higherst to lowest)
    chars_list.sort(reverse=True, key=sort_on)

    
    return chars_list