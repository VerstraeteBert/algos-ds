def gift_inschrijven(tuple, dictionarie):
    woord = str(tuple[:1])[1:-2].replace("'","")
    getal = float(str(tuple[1:])[1:-2])
    if woord in dictionarie:
        dictionarie[woord] += getal
    else:
        dictionarie[woord] = getal
    return dictionarie