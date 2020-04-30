def histogram(stenen):
    bib = {}
    for elem in stenen:
        bib[elem] = stenen.count(elem)
    
    return bib

def max_gelijk(stenen):
    aantal = []
    for elem in stenen:
        aantal.append(stenen.count(elem))
    
    return max(aantal)

def is_FullHouse(stenen):
    bib = histogram(stenen)
    full = False
    house = False
    for key in bib:
        if bib[key] == 3:
            full = True
        if bib[key] == 2:
            house = True
    
    if full and house:
        return True
        
    return False