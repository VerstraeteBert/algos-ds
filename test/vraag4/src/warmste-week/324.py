def gift_inschrijven(tuple, woordenlijst):
    check = 0
    for element in woordenlijst:
        if element == tuple[0]:
            woordenlijst[element] = woordenlijst[element] + tuple[-1]
            check = 1
    if check == 0:
        woordenlijst[tuple[0]] = tuple[-1]
    return woordenlijst
