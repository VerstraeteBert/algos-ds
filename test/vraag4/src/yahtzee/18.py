def som(lijst):
    waarde = 0
    for getal in lijst:
        waarde += getal
    return waarde


def is_Yathzee(lijst):
    if len(list(set(lijst))) == 1:
        return True
    return False


def is_grote_straat(lijst):
    lengte = len(lijst)
    lijst = sorted(list(set(lijst)))
    lengte2 = len(lijst)
    if lengte != lengte2:
        return False
    bereik = len(lijst) - 1
    for i in range(bereik):
        if lijst[i] + 1 != lijst[i + 1]:
            return False

    return True


def is_kleine_straat(lijst):
    if is_grote_straat(lijst):
        return True

    lengte = len(lijst)
    lijst = sorted(list(set(lijst)))
    lengte2 = len(lijst)
    if lengte != lengte2 + 1:
        return False
    bereik = len(lijst) - 1
    for i in range(bereik):
        if lijst[i] + 1 != lijst[i + 1]:
            return False

    return True

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