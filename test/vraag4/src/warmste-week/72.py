def gift_inschrijven(opbrengst, totaal):
    klas, bedrag = opbrengst
    if not klas in totaal:
        totaal[klas] = 0
    totaal[klas] += bedrag
    return totaal