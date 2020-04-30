def gift_inschrijven(gift, giftdict):
    klas = gift[0]
    bedrag = gift[1]
    try:
        bedrag = bedrag + giftdict[klas]
        giftdict[klas] = bedrag
    except KeyError:
        giftdict[klas] = bedrag
    return giftdict



