# Returns the total number of words in the given text.
# Splits on whitespace and counts resulting items.
def get_num_words(text):
    words = text.split()      # Break text into a list of words
    return len(words)         # Return how many words were found


# Counts occurrences of every character in the text.
# Characters are converted to lowercase for case-insensitive counting.
def count_characters(text):
    my_dict = {}              # Dictionary to store character frequency
    for characters in text:   # Iterate through every character in the text
        characters = characters.lower()   # Normalize to lowercase
        if characters in my_dict:         # If already seen, increment count
            my_dict[characters] = my_dict[characters] + 1
        else:                              # First time seeing this character
            my_dict[characters] = 1
    return my_dict            # Return the full frequency dictionary


# Helper function used for sorting character dictionaries.
# It extracts the "num" value so Python knows what to sort by.
def sort_on(item):
    return item["num"]        # Sorting key: the number of occurrences


# Converts the count dictionary into a list of {"char": ..., "num": ...}
# then sorts that list in descending order of frequency.
def sort_characters(count):
    sorted_ch = []            # List to store formatted character-count objects
    for ch, num in count.items():     # Loop through each character and its count
        sorted_ch.append({"char": ch, "num": num})  # Add structured dict entry

        # Sort after each insertion (not the most efficient, but untouched as requested)
        sorted_ch.sort(key=sort_on, reverse=True)

    return sorted_ch          # Return the fully sorted list
