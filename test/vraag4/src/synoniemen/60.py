def synoniemen(tekst, map):
    nieuw = []
    tekst_lijst = tekst.split()
    for woord in tekst_lijst:
        if woord in map:
            nieuw.append(map[woord])
        else:
            nieuw.append(woord)
    return " ".join(nieuw)