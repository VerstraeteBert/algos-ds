def synoniemen(tekst, woordenboek):
    woorden = []
    for woord in tekst.split():
        if woord in woordenboek:
            woorden.append(woordenboek[woord]) #het originele woord vervangen door een woord uit het woordenboek
        else:
            woorden.append(woord)
    #of eerst omzetten naar string en dan returnen: omzetten_naar_string=" ".join(woorden)
    omzetten_naar_string = " ".join(woorden)
    return omzetten_naar_string