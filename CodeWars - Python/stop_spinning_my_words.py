def spin_words(sentence):
    """Returns a sentence with words longer than 5 characters reversed."""
    
    words = sentence.split()

    for word in words:
        if len(word) >= 5:
            # Replaces normal word with the reversed word
            sentence = sentence.replace(word, word[::-1])

    return sentence