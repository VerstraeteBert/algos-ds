def synoniemen(tekst, woordenboek):
    woorden = tekst.split(" ")
    i = 0
    zin = ""
    while i in range(len(woorden)):
        woord = woorden[i]
        for woord in woordenboek.keys:
            woord = woordenboek[woord]
        zin += woord
        i += 1
    return zin