def histogram(stenen):
    stenen.sort()
    bib = {}
    for i in stenen:
        bib[i] = stenen.count(i)
    return bib

def max_gelijk(stenen):
    stenen.sort()
    bib = {}
    waarden = []
    for i in stenen:
        bib[i] = stenen.count(i)
    for i in bib.values():
        waarden.append(i)
    waarden.sort()
    return waarden[-1]

def is_FullHouse(stenen):
    stenen.sort()
    bib = {}
    waarden = []
    for i in stenen:
        bib[i] = stenen.count(i)
    for i in bib.values():
        waarden.append(i)
    waarden.sort(reverse = True)
    if waarden[0] == 3 and waarden[1] == 2:
        return True
    else:
        return False