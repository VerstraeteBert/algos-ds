def som(stenen):
    return sum(stenen)

def is_Yathzee(stenen):
    aantal_stenen = len(stenen)
    dobbelsteen1 = stenen[0]
    lijst = [dobbelsteen1]*aantal_stenen
    return stenen == lijst

def is_grote_straat(stenen):
    stenen = sorted(stenen)
    for item in stenen:
        if stenen.count(item) > 1:
            return False
    return stenen[-1] == stenen[0] + len(stenen) - 1

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
    histogram = {}
    for steen in sorted(stenen):
        if not steen in histogram:
            histogram[steen] = 1
        else:
            histogram[steen] += 1
    return histogram

def max_gelijk(stenen):
    hist = histogram(stenen)
    return max(hist.values())

def is_FullHouse(stenen):
    hist = histogram(stenen)
    controle = sorted(hist.values())
    return controle[0] == 2 and controle[1] == 3

def grootste_score(stenen):
    score = 0
    if is_Yathzee(stenen):
        score += 50
    elif is_grote_straat(stenen):
        score += 40
    elif is_kleine_straat(stenen):
        score += 30
    elif is_FullHouse(stenen):
        score += 25
    if som(stenen) > score:
        return som(stenen)
    else:
        return score