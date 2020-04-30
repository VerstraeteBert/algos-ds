def synoniemen(tekst, synoniemenboek):
    woorden = tekst.split()
    woorden_omgezet = []
    for w in woorden:
        if synoniemenboek.get(w) != None:
            woorden_omgezet.append(synoniemenboek[w])
        else:
            woorden_omgezet.append(w)
    return " ".join(woorden_omgezet)
