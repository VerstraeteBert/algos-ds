def som(stenen):
    return sum(stenen)
    
def is_Yathzee(stenen):
    stenen_gesorteerd = sorted(stenen)
    if stenen_gesorteerd[0] == stenen_gesorteerd[-1]:
        return True
    return False

def is_grote_straat(stenen):
    stenen_gesorteerd = sorted(stenen)
    for i in range(1, len(stenen_gesorteerd)):
        if stenen_gesorteerd[i] != stenen_gesorteerd[i-1] + 1:
            return False
    return True

def is_kleine_straat(stenen):
    stenen_gesorteerd = sorted(stenen)
    teller = 1
    for i in range(1, len(stenen_gesorteerd)):
        if stenen_gesorteerd[i] == stenen_gesorteerd[i-1] + 1:
            teller += 1
        else:
            if teller >= len(stenen_gesorteerd) - 1:
                return True
            if stenen_gesorteerd[i] != stenen_gesorteerd[i-1]:
                teller = 1
    return teller >= len(stenen)-1
    
def histogram(stenen):
    hist = {}
    for steen in sorted(stenen):
        if not steen in hist:
            hist[steen] = 1
        else:
            hist[steen] += 1
    return hist
    
def max_gelijk(stenen):
    hist = histogram(stenen)
    return max(hist.values())
    
def is_FullHouse(stenen):
    hist = histogram(stenen)
    aantallen = sorted(hist.values(), reverse = True)
    return aantallen[0] == 3 and aantallen[1] == 2
    
def grootste_score(stenen):
    score = 0
    if is_Yathzee(stenen):
        score = 50
    elif is_grote_straat(stenen):
        score = 40
    elif is_kleine_straat(stenen):
        score = 30
    elif is_FullHouse(stenen):
        score = 25
    totaal_ogen = sum(stenen)
    if totaal_ogen > score:
        score = totaal_ogen
    return score