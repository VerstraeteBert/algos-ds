# SYNONIEMEN

def synoniemen(zin, dict):
    nieuwe_zin = []
    zin_split = zin.split()
    for woord in zin_split:
        if woord in dict:
            nieuwe_zin.append(dict[woord])
        else:
            nieuwe_zin.append(woord)
    return " ".join(nieuwe_zin)