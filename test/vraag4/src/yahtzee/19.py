def som(stenen):
    som = 0
    for element in stenen:
        som += element
    return som


def is_Yathzee(stenen):
    eerste = stenen[0]
    zelfde = True
    for element in stenen:
        if element != eerste:
            zelfde = False
    return zelfde
    

def is_grote_straat(stenen):
    gr_straat = False
    stenen.sort()
    lst = []

    for i in range(0, len(stenen)-1):
        if stenen[i] == stenen[i + 1] - 1:
            lst.append(stenen[i])
            i += 1
        if i == len(stenen)-1 and stenen[i] == stenen[i - 1] + 1:
            lst.append(stenen[len(stenen)-1])

    if len(lst) >= len(stenen):
        gr_straat = True
    return gr_straat
    
    
def is_kleine_straat(stenen):
    kl_straat = False
    stenen.sort()
    aantal = 1
    gelijk = 0
    
    if is_grote_straat(stenen):
        kl_straat = True
    else:
        for i in range(0, len(stenen)-1):
            if aantal >= len(stenen)-1:
                kl_straat = True
            if stenen[i] == stenen[i + 1] - 1:
                aantal += 1
            elif stenen[i] == stenen[i+1]:
                gelijk += 1
            else:
                aantal = 1
            if i == len(stenen)-1 and stenen[i] == stenen[i - 1] + 1:
                aantal += 1
            
            i += 1
        if aantal >= len(stenen)-1:
            kl_straat = True

    return kl_straat
    
    
def histogram(stenen):
    hist = {}
    for worp in stenen:
        if worp not in hist.keys():
            hist[worp] = 1
        else:
            hist[worp] += 1
    return hist
    
    
def max_gelijk(stenen):
    hist = histogram(stenen)
    return max(hist.values())
    
    
def is_FullHouse(stenen):
    FH = False
    if len(stenen) == 5:
        hist = histogram(stenen)
        if 2 in hist.values() and 3 in hist.values():
            FH = True
    return FH
    
    
def grootste_score(stenen):
    punten = []
    if len(stenen) == 5:
        if is_Yathzee(stenen):
            punten.append(50)
        if is_FullHouse(stenen):
            punten.append(25)
        if is_grote_straat(stenen):
            punten.append(40)
        if is_kleine_straat(stenen):
            punten.append(30)
        punten.append(som(stenen))
    return max(punten)