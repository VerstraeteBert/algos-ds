def gift_inschrijven(nieuw, overzicht):
    klas, bedrag = nieuw
    if klas not in overzicht:
        overzicht[klas] = bedrag
    else:
        overzicht[klas] += bedrag
    return overzicht