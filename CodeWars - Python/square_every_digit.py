def square_digits(num):
    """Returns the square of every digit in a given number."""
    output = ""
    
    # integer to string conversion
    num_str = str(num)
    
    # iterates over each digit, squares it, and adds to string
    for number in num_str:
        output += str(int(number) ** 2)
        
    # conversion back to integer
    return int(output)