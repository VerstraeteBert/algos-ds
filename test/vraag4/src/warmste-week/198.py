def gift_inschrijven(gift, totaal): #string : float
    klas = str(gift[0])
    bedrag = float(gift[1])
    if klas in totaal:
        totaal[klas] += bedrag
    else:
        totaal[klas] = bedrag
    return totaal