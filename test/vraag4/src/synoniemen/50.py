def synoniemen(tekst, dictionary):
    tekst = tekst.split(' ')
    i = 0
    for woord in tekst:
        if woord in dictionary:
            tekst.remove(woord)
            tekst.insert(i, dictionary[woord])
        i += 1
    tekst = ' '.join(tekst)
    return tekst
    

    