def gift_inschrijven(gift, totaal):
    klas = gift[0]
    bedrag = gift[1]
    if klas in totaal:
        totaal[klas] += bedrag
    else:
        totaal[klas] = bedrag
    return totaal
