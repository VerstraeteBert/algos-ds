def synoniemen(zin, synoniemen):
    nieuwe_zin = ""
    for woord in zin.split():
        if woord in synoniemen:
            nieuwe_zin += synoniemen[woord] + " "
        else:
            nieuwe_zin += woord + " "
    return nieuwe_zin[:-1]