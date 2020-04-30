def histogram(stenen):
    stenen.sort()
    aantal_stenen = {}
    for i in range(0, len(stenen)):
            aantal_stenen[stenen[i]] = stenen.count(stenen[i])
    return aantal_stenen

def max_gelijk(stenen):
    max_aantal = 0
    for i in range(0, len(stenen)):
        if max_aantal < stenen.count(stenen[i]):
            max_aantal = stenen.count(stenen[i])
    return max_aantal

def is_FullHouse(stenen):
    stenen.sort()
    if stenen.count(stenen[0]) == 2:
        if stenen.count(stenen[2]) == 3:
            return True
        else:
            return False
    elif stenen.count(stenen[0]) == 3:
        if stenen.count(stenen[3]) == 2:
            return True
        else:
            return False
    else:
        return False

def som(stenen):
    som = sum(stenen)
    return som


def is_Yathzee(stenen):
    return len(set(stenen)) == 1


def is_grote_straat(stenen):
    # maxi = max(stenen)
    # mini = min(stenen)
    # lengte = len(stenen)
    # lengteset = len(set(stenen))
    if max(stenen) == min(stenen) + len(stenen) - 1 and len(set(stenen)) == len(stenen):
        return True
    return False


def is_kleine_straat(stenen):
    max1 = stenen[:]
    min1 = stenen[:]
    max1.remove(max(stenen))
    min1.remove(min(stenen))
    midden = set(stenen)
    if max(max1) == min(max1) + len(max1) - 1 and len(set(max1)) == len(
            max1):
        return True
    if max(min1) == min(min1) + len(min1) - 1 and len(set(min1)) == len(min1):
        return True
    if max(midden) == min(midden) + len(midden) - 1 and len(set(midden)) == len(stenen) - 1:
        return True
    return False

def grootste_score(stenen):
    score = 0
    if is_FullHouse(stenen) and score < 25:
        score = 25
    if is_Yathzee(stenen) and score < 50:
        score = 50
    if is_kleine_straat(stenen) and score < 30:
        score = 30
    if is_grote_straat(stenen) and score < 40:
        score = 40
    if score < som(stenen):
        score = som(stenen)
    return score