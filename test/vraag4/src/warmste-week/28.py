def gift_inschrijven(gift, bib):
    try:
        klas, geld = gift[:]
        bib[klas] += geld
    except KeyError:
        bib[klas] = geld
        
    return bib