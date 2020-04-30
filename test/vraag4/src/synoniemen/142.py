def synoniemen(tekst, woordenboek):
    tekst = tekst.split()
    tekst2 = str()
    for woord in  tekst:
        if woord in woordenboek:
            tekst2 += woordenboek[woord] + ' '
        else:
            tekst2 += woord + ' '
    tekst2 = tekst2[:-1]
    return tekst2