def synoniemen(tekst, woordenboek):
    tekstlijst = tekst.split()
    for index, woord in enumerate(tekstlijst):
        if woord in woordenboek:
            tekstlijst[index] = woordenboek[woord]
        else:
            continue
    return ' '.join(tekstlijst)

