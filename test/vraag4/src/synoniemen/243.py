def synoniemen(tekst, woordenboek):
    lijst = tekst.split()
    lijstnieuw = []
    for woord in lijst:
        if woord in woordenboek:
            woord = woordenboek[woord]
        lijstnieuw.append(woord)
    return " ".join(lijstnieuw)