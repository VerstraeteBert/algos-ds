def synoniemen(tekst, woordenboek):
    x = []
    for woord in tekst.split():
        if woord in woordenboek:
            x.append(woordenboek[woord])
        else:
            x.append(woord)
    return ' '.join(x)