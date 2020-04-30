def gift_inschrijven(klas, giften):
    if klas[0] in giften:
        giften.update({klas[0]: klas[1] + giften.get(klas[0])})
    else:
        giften.update({klas[0]: klas[1]})
    return giften