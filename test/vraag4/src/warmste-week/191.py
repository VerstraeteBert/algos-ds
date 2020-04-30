def gift_inschrijven(inschrijving, lijst):
    if inschrijving[0] in lijst:
        lijst[inschrijving[0]] += inschrijving[1]
    else:
        lijst[inschrijving[0]] = inschrijving[1]
    return lijst