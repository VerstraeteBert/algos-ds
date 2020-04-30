def synoniemen(zin, dictionnary):
    woorden = zin.split()
    for i in range(len(woorden)):
        if woorden[i] in dictionnary:
            woorden[i] = dictionnary[woorden[i]]
    return ' '.join(woorden)