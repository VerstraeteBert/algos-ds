def synoniemen(zin, dic_synoniemen):
    woorden = zin.split()
    nieuwe_zin = []
    for woord in woorden:
        if woord in dic_synoniemen:
            nieuwe_zin.append(dic_synoniemen[woord])
        else:
            nieuwe_zin.append(woord)
    return " ".join(nieuwe_zin)