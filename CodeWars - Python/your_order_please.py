def order(sentence):
    """Orders a string of words by the numbers they contain."""
    import re
    import copy
    
    # String to list with words as elements
    sentence = sentence.split()
    
    # Copy to preserve original
    new_sentence = copy.deepcopy(sentence)
    
    # Finds number contained in word and orders it in new list by number
    for word in sentence:
        num = re.findall(r'\d', word)[0]
        new_sentence[int(num) - 1] = word
        
    # List to string
    output = " ".join(map(str, new_sentence))

    return output