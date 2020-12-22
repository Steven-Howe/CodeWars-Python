def rgb(r, g, b):
    """Converts RGB values to 6-character hex value."""
    
    # Create list of values to iterate over
    values = [r, g, b]
    output = ""
    
    # Rounds values to nearest acceptable RGB value
    # Formats and combines into one 6-character length hex value
    for num in values:
        if num > 255:
            output += hex(255)[2:].rjust(2, "0")
        elif num < 0:
            output += hex(0)[2:].rjust(2, "0")
        else:
            output += hex(num)[2:].rjust(2, "0")
            
    return output.upper()