def histogram(stenen):
    stenen.sort()
    ok =""
    histo = {}
    for element in stenen:
        if str(element) not in ok:
            aantal = stenen.count(element)
            histo[element] = aantal
            ok += str(element)
    return histo