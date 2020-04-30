def synoniemen(zin, woordenboek):
    nieuw = []
    for woord in zin.split():
        if woord in woordenboek:
            nieuw.append(woordenboek[woord])
        else:
            nieuw.append(woord)
    return " ".join(nieuw)