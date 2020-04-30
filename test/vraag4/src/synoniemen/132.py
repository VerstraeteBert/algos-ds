def synoniemen(zin, synoniemen):
    nieuwe_zin = ''
    zin_list = zin.split()
    for i in range(0, len(zin_list)):
        if zin_list[i] in synoniemen.keys():
            nieuwe_zin += synoniemen[zin_list[i]] + ' '
        else:
            nieuwe_zin += zin_list[i] + ' '
    return nieuwe_zin[:-1]