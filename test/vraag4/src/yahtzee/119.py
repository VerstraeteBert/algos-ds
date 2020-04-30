def histogram(stenen):
    stenen.sort()
    histogram = {}
    for waarde in stenen:
        if waarde in histogram:
            histogram[waarde] += 1
        else:
            histogram[waarde] = 1
    return histogram
def max_gelijk(stenen):
    dict = histogram(stenen)
    hoogst = max(dict.values())
    return hoogst
def is_FullHouse(stenen):
    dict = histogram(stenen)
    if max_gelijk(stenen) != 3:
        return False
    if min(dict.values()) != 2:
        return False
    return True
def som(stenen):
    som = sum(stenen)
    return som
def is_Yathzee(stenen):
    steen = stenen[0]
    for element in stenen:
        if element != steen:
            return False
        steen = element
    return True
def is_grote_straat(stenen):
    stenen.sort()
    vorig = stenen[0]
    for i in range(1, len(stenen)):
        verschil = stenen[i] - vorig
        if verschil != 1:
            return False
        vorig = stenen[i]
    return True
def is_kleine_straat(stenen):
    if is_grote_straat(stenen):
        return True
    stenen.sort()
    for element in stenen:
        lijst = stenen[:]
        lijst.remove(element)
        if is_grote_straat(lijst):
            return True
    return False
def grootste_score(stenen):
    score = 0
    som = 0
    if is_Yathzee(stenen):
        score = 50
    elif is_grote_straat(stenen):
        score = 40
    elif is_kleine_straat(stenen):
        score = 30
    elif is_FullHouse(stenen):
        score = 25
    for steen in stenen:
        som += steen
    if som > score:
        return som
    return score