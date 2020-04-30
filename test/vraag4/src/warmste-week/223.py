def gift_inschrijven(bedrag, totaal):
    if bedrag[0] in totaal:
        totaal[bedrag[0]] += bedrag[1]
    else:
        totaal[bedrag[0]] = bedrag[1]
    return totaal