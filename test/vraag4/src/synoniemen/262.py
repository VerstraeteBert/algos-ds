def synoniemen(tekst, woordenboek):
    woorden = []
    for woord in tekst.split():
        if woord in woordenboek:
            woorden.append(woordenboek[woord])
        else:
            woorden.append(woord)
    return " ".join(woorden)


#alternatieve oplossing
def synoniemen(tekst, woordenboek):
    woorden = tekst.split()
    for i in range(len(woorden)):
        if woorden[i] in woordenboek:
            woorden[i] = woordenboek[woorden[i]]
    return " ".join(woorden)