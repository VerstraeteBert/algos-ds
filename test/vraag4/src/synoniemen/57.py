def synoniemen(zin,woordenboek):
    woorden = zin.split()
    for i in range (len(woorden)):
        if woorden[i] in woordenboek:
            woorden [i] = woordenboek[woorden[i]]
    return ' '.join(woorden)