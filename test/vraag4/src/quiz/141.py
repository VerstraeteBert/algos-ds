def verlaat_ploeg(verlater, ploeg, book):
    if len(book[ploeg])>1:
        book[ploeg].remove(verlater)
    else:
        del book[ploeg]
    return book
def vervoegt_ploeg(vervoeger, ploeg, book):
    if ploeg in book.keys():
        book[ploeg].append(vervoeger)
    else:
        book[ploeg] = [vervoeger]
    return book