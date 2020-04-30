def synoniemen(tekst, woordenboek):
    woorden = tekst.split(' ')
    uitvoer = ''
    for teller in range(0, len(woorden)):
        woord = woorden[teller]

        if woord in woordenboek:
            uitvoer += woordenboek[woord] + ' '
        else:
            uitvoer += woord + ' '

    return uitvoer.strip()