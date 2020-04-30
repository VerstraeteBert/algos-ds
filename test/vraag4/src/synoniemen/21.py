def synoniemen(zin, dictinary):
    zin = zin.split()
    string = ""
    for woord in zin:
        if woord in dictinary.keys():
            string += dictinary[woord] + " "
        else:
            string += woord+" "
    return string.strip()