def open_or_senior(data):
    membership = []
    
    # If age is 55 or greater and handicap greater than 7 then member is a Senior, otherwise member is Open
    for item in data:
        if (item[0] >= 55) and (item[1] > 7):
            membership.append("Senior")
        else:
            membership.append("Open")
    
    return membership