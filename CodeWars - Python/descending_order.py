def descending_order(num):
    """Returns an int in descending order."""
    
    num_list = []
    num_str = ""
    
    # Convert to string to allow for iteration and then list to allow for reversed sort method
    for n in str(num):
        num_list.append(n)
    num_list.sort(reverse=True)
    
    # Convert list back to a string
    for n in num_list:
        num_str += n
    
    # Convert string back to an int
    return int(num_str)