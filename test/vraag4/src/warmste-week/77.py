def gift_inschrijven(gift, overzicht):
    if gift[0] in overzicht.keys():
        overzicht[gift[0]] = overzicht[gift[0]] + gift[1]
    else:
        overzicht[gift[0]] = gift[1]
    return overzicht