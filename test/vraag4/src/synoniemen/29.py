def synoniemen(zin, woordenboek):
    n_zin = ""
    for woord in zin.split(" "):
        if woord in woordenboek:
            n_zin += woordenboek[woord] + " "
        else:
            n_zin += woord + " "
    return n_zin[:-1]