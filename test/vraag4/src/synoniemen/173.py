def synoniemen(zin, reeks):
    zin = zin.split()
    nieuw = ""
    for i in range(len(zin)):
        woord = zin[i]
        if woord in reeks:
            zin[i] = reeks[woord]
        nieuw += zin[i] + " "
    return nieuw.strip(' ')