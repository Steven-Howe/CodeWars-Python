def find_outlier(integers):
    """Finds the only even or odd number for a given list of integers."""
    
    count_even = 0
    count_odd = 0

    # Determines if list is majority even or odd
    for x in integers[::2]:
        if x % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
            
    # Finds even number if the list is majority odd
    if count_odd >= 2:
        for x in integers:
            if x % 2 == 0:
                return x
            
    # Finds odd number if the list is majority even
    else:
        for x in integers:
            if x % 2 == 1:
                return x