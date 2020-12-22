def two_sum(numbers, target):
    """Finds two numbers in an array that add up to the sum of the given integer."""
    
    # Iterates through list to find b, as in b = target - a
    for i, num in enumerate(numbers):
        if target - num in numbers:
            
            # Returns indexes of numbers whose sum equals the target
            return (i, numbers.index((target - num), i + 1))