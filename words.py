def print_upper_words(words):
    """Accepts a list of words and prints each word in uppercase on a separate line"""
    
    for word in words:
        modified_string = word.upper()
        print(modified_string)

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

def print_upper_words_start_with_e(words):
    """Accepts a list of words and prints the word in uppercase on a separate line 
    if it starts with an e (uppercase or lowercase)"""

    for word in words:
        lower_string = word.lower()
        upper_string = word.upper()
        if lower_string[0] == "e":
            print(upper_string)

print_upper_words_start_with_e(["Exciting", "enthrall", "hammer", "python", "eager"])

def print_upper_words_start_with_letters(words, must_start_with):
    """Accepts a list of words and prints the words in uppercase on a separate line
    if the word starts with any of the letters listed in the set"""

    for word in words:
        lower_string = word.lower()
        upper_string = word.upper()
        for letter in must_start_with:
            if letter == lower_string[0] or letter == upper_string[0]:
                print(upper_string)

print_upper_words_start_with_letters(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})