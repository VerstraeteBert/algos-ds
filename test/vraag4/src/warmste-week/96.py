def gift_inschrijven(bedragklas, alles):
    klas = bedragklas[0]
    gift = bedragklas[1]
    if klas in alles:
        oorspronkelijk = alles[klas]
        alles[klas] = float(gift) + float(oorspronkelijk)
    else:
        alles[klas] = gift
    return alles