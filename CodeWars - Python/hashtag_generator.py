def generate_hashtag(s):
    """Converts a string to a hashtag social media format."""
    
    # Capitalizes the first letter of each word
    hashtag = s.title()
    
    # Gets rid of spaces and prepends hashtag
    hashtag = hashtag.replace(" ", "")
    hashtag = "#" + hashtag
    
    # String must be under 140 characters long
    if len(hashtag) > 140 or hashtag == "#":
        return False
    else:
        return hashtag