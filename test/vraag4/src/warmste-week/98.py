def gift_inschrijven(extra, totaal):
    klas, bedrag = extra
    if klas in totaal:
        totaal[klas] += bedrag
    else:
        totaal[klas] = bedrag
    return totaal
    