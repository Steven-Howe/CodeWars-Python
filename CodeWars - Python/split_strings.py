def solution(s):
    """Splits a string into pairs and adds an underscore to last pair if odd amount."""
     
    my_list = []
    
    # Sets beginning string indexes
    begin = 0
    end = 2
   
    # Splits every two characters and adds to a list
    while begin < len(s) - 1:
        my_slice = s[begin:end]
        my_list.append(my_slice)
        
        # Increments string indexes
        begin += 2
        end += 2
    
    # If odd length then an underscore is added
    if (len(s) % 2 != 0):
        my_slice = s[-1] + "_"
        my_list.append(my_slice)
        
    return my_list