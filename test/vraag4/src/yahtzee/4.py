def som(stenen):
    return sum(stenen)


def is_Yathzee(stenen):
    stenen.sort()
    return stenen[0] == stenen[-1]


def is_grote_straat(stenen):
    stenen.sort()
    for i in range(1, len(stenen)):
        if stenen[i] != stenen[i - 1] + 1:
            return False
    return True


def is_kleine_straat(stenen):
    stenen.sort()
    teller = 1
    for i in range(1, len(stenen)):
        if stenen[i] == stenen[i - 1] + 1:
            teller += 1
        else:
            if teller >= len(stenen) - 1:
                return True
            if stenen[i] != stenen[i - 1]:
                teller = 1
    return teller >= len(stenen) - 1


def histogram(stenen):
    stenen.sort()
    histo = {}
    for steen in stenen:
        if steen not in histo:
            histo[steen] = 1
        else:
            histo[steen] += 1
    return histo


def max_gelijk(stenen):
    histo = histogram(stenen)
    return max(histo.values())


def is_FullHouse(stenen):
    histo = histogram(stenen)
    aantallen = sorted(histo.values(), reverse=True)
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
