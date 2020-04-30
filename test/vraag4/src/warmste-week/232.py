def gift_inschrijven(klas, dict):
    if klas[0] in dict.keys():
        dict[klas[0]] += klas[1]
        
    else:
        dict[klas[0]] = klas[1]
    return dict