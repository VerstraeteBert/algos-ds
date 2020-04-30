def synoniemen(zin, synoniemwoordenboek):
    woorden = zin.split(" ")        # maakt een lijst van de woorden in de zin
    zin_nieuw = []
    for woord in woorden:
        if woord in synoniemwoordenboek:
            zin_nieuw.append(synoniemwoordenboek[woord])
        else:
            zin_nieuw.append(woord)
    return " ".join(zin_nieuw)
