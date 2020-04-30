def gift_inschrijven(tuple, book):
    klas, bedrag = tuple
    bedrag = float(bedrag)
    if klas in book.keys():
        book[klas]+= bedrag
    else:
        book[klas] = bedrag
    return book