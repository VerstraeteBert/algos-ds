def synoniemen(tekst, dictionarie):
    lijst = tekst.split(" ")
    lengte = len(lijst)
    zin = ""
    for k in range(lengte):
        woord = lijst[k]
        if woord in dictionarie:
            zin += dictionarie[woord] + " "
        else:
            zin += woord + " "
    return (zin[:-1])