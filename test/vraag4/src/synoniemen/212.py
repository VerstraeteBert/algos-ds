def synoniemen(tekst, woordenboek):
    woordenboek = dict(woordenboek)

    for woord in tekst.split():
        if woord in woordenboek:
            tekst = str(tekst).replace(woord, woordenboek[woord])

    return tekst

