def synoniemen(zin, dictionary):
    zin = zin.split()
    x = 0
    for i in zin:
        if i in dictionary:
         zin[x] = dictionary[i]
        x += 1
    zin = ' '.join(zin)
    return zin

