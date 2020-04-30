def synoniemen(zin, woordenboek):
    zin = zin.split()
    nieuwe_zin = ""
    for woord in zin:
        if woord in woordenboek:
            woord = woordenboek[woord]
        nieuwe_zin += woord + " "
    return nieuwe_zin.strip(" ")