import re

def increment_string(strng):
    """Takes a string and increments the ending number by 1."""
    
    # Will append a 1 if string is empty or doesn't have an ending number
    if strng == "" or not strng[-1].isdigit():
        return strng + "1"
    else:
        # Finds the ending digits in the string
        nums = re.search(r'\d*$', strng).group()
        
        # Increments number by 1 while preserving leading zeros
        new_nums = str(int(nums) + 1).zfill(len(nums))
        
        # Returns string with new number
        return strng.replace(nums, new_nums)