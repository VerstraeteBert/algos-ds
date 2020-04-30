def synoniemen(zin, synoniemen):
    nieuwe_zin = ' '.join([synoniemen.get(i, i) for i in zin.split()])
    return nieuwe_zin
