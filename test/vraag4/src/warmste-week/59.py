def gift_inschrijven(gift, giftdict):
    klas = gift[0]
    bedrag = gift[1]
    try:
        bedrag = bedrag + giftdict[klas]
        giftdict[klas] = bedrag
    except KeyError:
        giftdict[klas] = bedrag
    return giftdict


print(gift_inschrijven(('5WWI', 78.33),{'6WWI': 64.87, '6BI': 71.63, '5BI': 26.39, '5WWI': 82.68}))