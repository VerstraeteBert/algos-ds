def synoniemen(tekst, woordenboek):
    zin = tekst.split()
    nzin = ""
    for woord in zin:
        if woord in woordenboek:
            woord = woordenboek[woord]
        nzin += woord + ' '
    return nzin[:-1]
