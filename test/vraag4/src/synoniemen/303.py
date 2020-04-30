def synoniemen(zin, dictionary):
    zin2 = list(zin.split(' '))
    for i in range(0, len(zin)):
        try:
            if zin2[i] in dictionary:
                zin = zin.replace(zin2[i], dictionary[zin2[i]])
            else:
                i += 1
        except IndexError:
            break
    return zin