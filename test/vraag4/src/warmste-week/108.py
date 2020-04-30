def gift_inschrijven(bedrag, totaal):
    klas = bedrag[0]
    gift = bedrag[1]
    if klas in totaal:
        gift2 = totaal[klas]
        gift3 = gift + gift2
        totaal[klas] = gift3
    else:
        totaal[klas] = gift
    return totaal