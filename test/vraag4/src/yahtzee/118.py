def som(stenen):
    som = sum(stenen)
    return som
    
def is_Yathzee(stenen):
    sorteer = sorted(stenen)
    return sorteer[0] == sorteer[-1]

def is_grote_straat(stenen):
    sorteer = sorted(stenen)
    for i in range(1, len(sorteer)):
        if sorteer[i] != sorteer[i - 1] + 1:
            return False
    return True

def is_kleine_straat(stenen):
    gesorteerde_stenen = sorted(stenen)
    tel = 1
    for i in range(1, len(gesorteerde_stenen)):
        if gesorteerde_stenen[i] == gesorteerde_stenen[i - 1] + 1:
            tel += 1
        else:
            if tel >= len(gesorteerde_stenen) - 1:
                return True
            if gesorteerde_stenen[i] != gesorteerde_stenen[i - 1]:
                tel = 1
    return tel >= len(stenen) - 1


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
    aantallen = sorted(hist.values(), reverse=True)
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
