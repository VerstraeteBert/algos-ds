def synoniemen(zin,dict):
    woordenlijst = zin.split()
    eindzin = []
    for woord in woordenlijst:
        if woord in dict:
            eindzin.append(dict[woord])
        else:
            eindzin.append(woord)
    return " ".join(eindzin)