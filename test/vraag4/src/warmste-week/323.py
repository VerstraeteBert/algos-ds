def gift_inschrijven(gift, giftdict):
    klas = gift[0]
    bedrag = gift[1]
    if klas in giftdict:
        bedrag = bedrag + giftdict[klas]
        giftdict[klas] = bedrag
    else:
        giftdict[klas] = bedrag
    return giftdict
