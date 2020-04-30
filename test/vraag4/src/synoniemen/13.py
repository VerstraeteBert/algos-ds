def synoniemen(tekst, woordenboek):
    zin = tekst.split()
    nieuwe_zin = ""
    for woord in zin:
        if woord in woordenboek:
            nieuwe_zin += woordenboek[woord] + ' '
        else:
            nieuwe_zin += woord + ' '
    return nieuwe_zin.rstrip(' ')
