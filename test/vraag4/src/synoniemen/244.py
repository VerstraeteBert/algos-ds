def synoniemen(tekst, synoniemen):
    woorden = tekst.split(' ')
    for i in range(len(woorden)):
        if woorden[i] in synoniemen:
            woorden[i] = synoniemen[woorden[i]]
    return ' '.join(woorden)