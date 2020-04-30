def synoniemen(tekst, woordenboek):
    tekst = tekst.split()
    tekst2 = ''
    for woord in tekst:
        if woord in woordenboek:
            tekst2 += woordenboek[woord] + ' '
        else:
            tekst2 += woord + ' '
    return tekst2[:-1]