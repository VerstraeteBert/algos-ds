def synoniemen(zin , woordenboek):
    zin2 = zin.split()
    nieuwe_zin = ""
    for woord in zin2:
        if woord in woordenboek:
            woord = woordenboek[woord]
            nieuwe_zin = nieuwe_zin + " " + woord
        else:
            nieuwe_zin = nieuwe_zin + " " + woord
    return nieuwe_zin[1:]