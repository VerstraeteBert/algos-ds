def synoniemen(tekst, dictionairy):
    tekst_strip = tekst.strip()
    gescheiden = tekst.split()
    woorden = []
    for word in gescheiden:
        if word in dictionairy:
            woorden.append(dictionairy[word])
        else:
            woorden.append(word)
    return " ".join(woorden)