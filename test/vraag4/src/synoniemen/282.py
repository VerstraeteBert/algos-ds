def synoniemen(tekst, synoniemenwoordenboek):
    antwoord = []
    tekst_lijst = tekst.split(' ')
    for woord in tekst_lijst:
        if woord in synoniemenwoordenboek:
            antwoord.append(synoniemenwoordenboek[woord])
        else:
            antwoord.append(woord)
    return ' '.join(antwoord)