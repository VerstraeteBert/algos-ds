def synoniemen(tekst, d):
    tekst1 = ""
    woorden = tekst.split(" ")
    for woord in woorden:
        if woord in d:
            tekst1 += d[woord]
            tekst1 += " "
        else:
            tekst1 += woord
            tekst1 += " "
    tekst1 = tekst1[:-1]
    return tekst1