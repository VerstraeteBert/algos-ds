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
            