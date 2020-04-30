def synoniemen(zin,synoniemenlijst):
    lijst_met_woorden=zin.split(" ")
    aangepast_lijst=[]
    for i in range(len(lijst_met_woorden)):
        woord=lijst_met_woorden[i]
        if woord in synoniemenlijst:
            aangepast_lijst.append(synoniemenlijst[woord])
        else:
            aangepast_lijst.append(woord)
    return " ".join(aangepast_lijst)