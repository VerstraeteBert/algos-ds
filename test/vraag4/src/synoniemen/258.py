def synoniemen(zin, dic):
    woorden = []
    for woord in zin.split():
        if woord in dic:
            woorden.append(dic[woord])
        else:
            woorden.append(woord)
    return ' '.join(woorden)