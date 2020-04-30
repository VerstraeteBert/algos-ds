def synoniemen(tekst,woordenboek):

    zin = ""
    for woord in tekst.split():
        if woord in woordenboek:
            woord = woordenboek[woord]
        zin += woord
        zin += " "
    zin = zin.strip()
    return zin

