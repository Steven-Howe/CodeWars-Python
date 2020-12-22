import re

def to_camel_case(text):
    """Changes text input into Upper Camel Case."""
    
    # Returns string if empty
    if text == "":
        return text
    
    # Uses delimiters of - and _
    words = re.split('\-|_', text)

    output = ""
    
    # Capitalizes the first letter of every other word besides the first
    for word in words:
        if word == words[0]:
            output += word
        else:
            capitalized_word = word.capitalize()
            output += capitalized_word

    return output