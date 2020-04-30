def gift_inschrijven(tuple, giften):
    if tuple[0] in giften.keys():
        som = tuple[1] + giften[tuple[0]]
        giften[tuple[0]] = som
    else:
        giften[tuple[0]] = tuple[1]
    return giften