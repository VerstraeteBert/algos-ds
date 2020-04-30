def synoniemen(tekst, wb):
    woorden = tekst.split()
    nieuwezin = []
    for woord in woorden:
        if woord in wb:
            nieuwezin.append(wb[woord])
        else:
            nieuwezin.append(woord)
    resultaat = ' '.join(nieuwezin)
    return resultaat