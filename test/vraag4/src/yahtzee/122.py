def som(stenen):
    return sum(stenen)

def is_Yathzee(stenen):
    gesorteerd = sorted(stenen)
    return gesorteerd[0] == gesorteerd[-1]

def is_grote_straat(stenen):
    lengte = len(stenen)
    gesorteerd = sorted(stenen)
    antwoord = True
    i = 0
    while i in range(lengte-1):
        if gesorteerd[i] + 1 != gesorteerd[i+1]:
            antwoord = False
        i += 1
    return antwoord

def is_kleine_straat(stenen):
    lengte = len(stenen)
    gesorteerd = sorted(stenen)
    tel = 0
    i = 0
    while i in range(lengte - 1):
        if gesorteerd[i] + 1 == gesorteerd[i + 1]:
            tel += 1
        i += 1
    voorwaarde_1 = gesorteerd[0] +1 != gesorteerd[1]
    voorwaarde_2 = gesorteerd[-2] +1 != gesorteerd[-1]
    verschil = int(gesorteerd[-1]) - int(gesorteerd[0])
    voorwaarde_3 = lengte - 2 == verschil
    if tel == lengte -2:
        return voorwaarde_1 or voorwaarde_2 or voorwaarde_3
    if tel == lengte -1:
        return True
    else:
        return False

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
        return 50
    if is_grote_straat(stenen):
        return 40
    if is_kleine_straat(stenen):
        return 30
    score = som(stenen)
    if score >= 25:
        return score
    if is_FullHouse(stenen):
        return 25
    return score




