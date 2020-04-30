def gift_inschrijven(tuple, dictionary):
    l = len(tuple)
    bedrag = float(tuple[l-1])
    klas = tuple[0]
    if klas in dictionary:
        bedrag1 = float(dictionary[klas])
        bedragtot = bedrag + bedrag1
        dictionary[klas] = float(bedragtot)
        return(dictionary)
    else:
        dictionary[klas] = bedrag
        return(dictionary)
        
    
    
    