def synoniemen(zin,wb):
    zin=zin.split(" ")
    for i in range(len(zin)):
        if zin[i] in wb:
            zin[i]=wb[zin[i]]
        zin[i]=zin[i]+" "
    zin="".join(zin)
    return zin[:-1]
    