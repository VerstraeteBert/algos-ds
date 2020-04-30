def gift_inschrijven(bedrag, lijst):
    if bedrag[0] in lijst.keys():
        s = lijst[bedrag[0]] + bedrag[1]
        lijst[bedrag[0]] = s
    else:
        lijst[bedrag[0]] = bedrag[1]
    return lijst