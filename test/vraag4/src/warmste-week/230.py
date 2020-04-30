def gift_inschrijven(niewklastuple, dictionarie):
    klas, gift = niewklastuple
    if not klas in dictionarie:
        dictionarie[klas] = gift
    else:
        dictionarie[klas] += gift
    return dictionarie
