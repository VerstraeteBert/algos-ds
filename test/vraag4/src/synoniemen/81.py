def synoniemen(tekst, synoniem):
    woorden = tekst.split()
    for woord in woorden:
        if woord in synoniem:
            woorden[woorden.index(woord)] = synoniem[woord]
    tekst2 = " ".join(woorden)
    return tekst2