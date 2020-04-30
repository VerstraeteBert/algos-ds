def synoniemen(tekst, w):
    res = ''
    nieuwe_tekst = tekst.split(' ')
    for woord in nieuwe_tekst:
        if woord not in w:
            res += woord + ' '
        else:
            res += w[woord] + ' '
    return res[0:-1]