def synoniemen(zin, dic):
    woorden = zin.split(" ")
    k = 0
    for x in woorden:
        if x in dic:
            woorden[k] = dic[x]
        k += 1
    zin = " ".join(woorden)
    return zin