def gift_inschrijven(nieuw, giften):
    key, value = nieuw
    if not key in giften:
        giften[key] = 0
    giften[key] += value
    return giften