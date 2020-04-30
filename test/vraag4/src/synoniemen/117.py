def synoniemen(tekst, woordenboek):
    tekstlijst = tekst.split(' ')
    for index, woord in enumerate(tekstlijst):
        try:
            tekstlijst[index] = woordenboek[woord]
        except KeyError:
            continue
    return ' '.join(tekstlijst)