def synoniemen(zin, book):
    zin = zin.lower()
    lijst = zin.split()
    nieuw = []
    for woord in lijst:
        if woord in book.keys():
            nieuw.append(book[woord])
        else:
            nieuw.append(woord)
    return " ".join(nieuw)