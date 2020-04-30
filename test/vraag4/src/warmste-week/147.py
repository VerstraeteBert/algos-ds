def gift_inschrijven(extra_gift, giften):
    if extra_gift[0] in giften:
        giften[extra_gift[0]] += extra_gift[1]
    else:
        giften[extra_gift[0]] = extra_gift[1]
    return giften