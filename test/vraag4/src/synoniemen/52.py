def synoniemen(zin, synoniemen):
    zin= zin.split(" ")
    for element in zin:
        zin.remove(element).append(synoniemen[element])
    return zin
    
    