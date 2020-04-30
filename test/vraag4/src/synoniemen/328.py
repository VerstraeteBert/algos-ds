def synoniemen(zin, synoniemen):
    zin = zin.split(' ')
    nieuwe_zin = ''
    for i in range(len(zin)):
        if zin[i] in synoniemen:
            nieuwe_zin += synoniemen[zin[i]] + ' '
        else:
            nieuwe_zin += zin[i] + ' '
    nieuwe_zin = nieuwe_zin.strip()
    return nieuwe_zin
