def synoniemen(zin, dict):
    lst = zin.split(" ")
    for i in range(0, len(lst)):
        if lst[i] in dict:
            lst[i] = dict[lst[i]]
    zin2 = " ".join(lst)
    return zin2
    