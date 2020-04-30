def synoniemen(zin, woordenboek):
    woord = zin.split()      #maakt een lijst aan met 1 woord = 1 element
    for i in range(len(woord)):
        if woord[i] in woordenboek:
            woord[i] = woordenboek[woord[i]]
        else:
            woord[i] = woord[i]
        tekst = " ".join(woord)
    return tekst