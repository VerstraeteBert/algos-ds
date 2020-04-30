def synoniemen(zin, dict):
    zin = zin.split()
    for i in range(len(zin)):
        if zin[i] in dict:
            zin[i] = dict[zin[i]]

    return " ".join(zin)
