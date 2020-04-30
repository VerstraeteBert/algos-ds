
def som(stenen):
    return sum(stenen)


def is_Yathzee(stenen):
    is_yath = False
    getal_ = stenen[0]
    for getal in stenen:
        if getal_ == int(getal):
            is_yath = True
        else:
            is_yath = False
            break
        getal_ = int(getal)

    return is_yath


def is_grote_straat(stenen):
    stenen.sort()
    for i in range(stenen[0], len(stenen) + stenen[0]):
        if i == stenen[i - stenen[0]]:
            pass
        else:
            return False

    return True


def is_kleine_straat(stenen):
    if is_grote_straat(stenen):
        return True

    lengte = len(stenen)

    stenen.sort()

    for i in range(stenen[0], len(stenen) + stenen[0]):
        if stenen.count(i) > 1:
            stenen.pop(stenen.index(i))

    amount_correct = 0

    if stenen[0] == 1 and stenen[1] != 2:
        stenen.pop(0)

    for i in range(stenen[0], len(stenen) + stenen[0]):
        if i == stenen[i - stenen[0]]:
            amount_correct += 1

    if amount_correct >= (lengte - 1):
        return True
    return False



def histogram(stenen):
    geworpen = {}
    stenen.sort()

    for worp in stenen:
        if worp not in geworpen:
            geworpen[worp] = 1
        else:
            geworpen[worp] += 1

    return geworpen

def max_gelijk(stenen):
    hist = histogram(stenen)

    hoogste = {"worp": 0, "aantal": 0}

    for steen, aantal in hist.items():
        if aantal > hoogste["aantal"]:
            hoogste["worp"] = steen
            hoogste["aantal"] = aantal

    return hoogste["aantal"]


def is_FullHouse(stenen):
    hist = histogram(stenen)

    if len(hist) > 2:
        return False

    worpen = []

    for key in hist.keys():
        worpen.append(key)

    try:
        if hist[worpen[0]] == 2 and hist[worpen[1]] == 3:
            return True
        if hist[worpen[1]] == 2 and hist[worpen[0]] == 3:
            return True
    except:
        pass

    return False

import copy

def grootste_score(stenen):
    scores = {"drie": 0, "vier": 0, "kleine": 0, "grote": 0, "full": 0, "kans": 0, "yahtz": 0}
    stenen_temp = copy.deepcopy(stenen)
    som_ = som(stenen)
    hist = histogram(stenen)

    has_four = False
    has_drie = False
    for val in hist.values():
        if val == 4:
            has_four = True
        if val == 3:
            has_drie = True

    if has_drie:
        scores["drie"] += som_
    elif has_four:
        scores["vier"] += som_

    if is_kleine_straat(stenen_temp):
        scores["kleine"] += 30
    stenen_temp = copy.deepcopy(stenen)
    if is_grote_straat(stenen_temp):
        scores["grote"] += 40
    stenen_temp = copy.deepcopy(stenen)
    if is_FullHouse(stenen_temp):
        scores["full"] += 25
    scores["kans"] += som_

    stenen_temp = copy.deepcopy(stenen)

    if is_Yathzee(stenen_temp):
        scores["yahtz"] += 50

    return max(scores.values())

