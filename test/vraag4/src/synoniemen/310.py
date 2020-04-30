def synoniemen(tekst, woordenboek):
    woorden = []
    for i in tekst.split():
        if i in woordenboek:
            woorden.append(woordenboek[i])
        else:
            woorden.append(i)
    return ' '.join(woorden)