def synoniemen(zin, synoniemen):
    lzin = zin.split()
    # print(lzin)  # test
    for i in lzin:
        # print(i)  # test
        if i in synoniemen:
            # print(synoniemen[i])  # test
            j = lzin.index(i)
            lzin[j] = synoniemen[i]
    # print(lzin)  # test
    zin = ""
    for k in lzin:
        zin += " " + k
    zin = zin[1::]
    return zin
