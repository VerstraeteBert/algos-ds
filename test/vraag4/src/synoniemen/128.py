def synoniemen(tekst, woordenboek):
    nieuw = []
    for woord in tekst.split():
        if woord in woordenboek:
            nieuw.append(woordenboek[woord])
        else:
            nieuw.append(woord)
    return " ".join(nieuw)