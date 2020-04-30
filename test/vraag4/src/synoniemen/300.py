def synoniemen(zin, wb):
    resultaat = ""
    for woord in zin.split():
        if woord in wb:
            resultaat += wb[woord] + " "
        else:
            resultaat += woord + " "
    return resultaat[:-1]