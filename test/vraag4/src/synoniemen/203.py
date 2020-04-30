def synoniemen(zin, dic):
    zin=zin.split()
    zin2=''
    for i in zin:
        if i not in dic:
            zin2+=i+ ' '
        if i in dic:
            zin2+=dic[i]+ ' '
    return zin2.strip()