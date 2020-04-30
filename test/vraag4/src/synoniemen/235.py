def synoniemen(zin, syno):
    nieuwe_zin = ' '.join([syno.get(i, i) for i in zin.split()])
    return nieuwe_zin