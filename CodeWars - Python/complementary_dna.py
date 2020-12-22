def DNA_strand(dna):
    """Returns the complement side of a given DNA strand."""
    
    complement = ""
    
    # Matches the complement of the individual instruction
    for strand in dna:
        if strand == "A":
            complement += "T"
        elif strand == "T":
            complement += "A"
        elif strand == "C":
            complement += "G"
        else:
            complement += "C"

    return complement