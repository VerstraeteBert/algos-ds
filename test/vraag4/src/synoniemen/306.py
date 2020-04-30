def synoniemen(zin,dict):
    l1, l2 = zin.split(" "), []
    for woord in l1:
        if woord not in dict:
            l2.append(woord)
        else:
            l2.append(dict[woord])
    result = ' '.join(l2)
    return result