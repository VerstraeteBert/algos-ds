def synoniemen(tekst, dict):
    zin = []
    for woord in tekst.split():
        if woord in dict:
            zin.append(dict[woord])
        else:
            zin.append(woord)
    return " ".join(zin)