def synoniemen(zin, sleutel):
    lijst = zin.split()
    zin = ""
    for item in lijst:
        if item in sleutel:
            zin += sleutel[item] + " "
        else:
            zin += item + " "
    return zin.strip()
