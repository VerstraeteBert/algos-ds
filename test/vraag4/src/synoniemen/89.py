
def synoniemen(zin, woordenboek):
    nieuwe_zin = " ".join([woordenboek.get(i, i) for i in zin.split()])
    return nieuwe_zin