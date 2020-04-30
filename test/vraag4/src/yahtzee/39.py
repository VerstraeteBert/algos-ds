def histogram(stenen):
    dic = {}
    for x in stenen:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    return dic

def max_gelijk(stenen):
    aantal = histogram(stenen)
    maxi = 0
    for x in aantal:
        y = aantal[x]
        maxi = max(maxi, y)
    return maxi

def is_FullHouse(stenen):
    aantal = histogram(stenen)
    full = True
    for x in aantal:
        if not aantal[x] in (2, 3):
            full = False
    return full
    
def grootste_score(stenen):
    stenen.sort()
    aantal = histogram(stenen)
    score = 0
    for x in aantal:
        if aantal[x] == 5:
            score = max(score, 50)
    score = max(score, sum(stenen))
    if is_FullHouse(stenen):
        score = max(score, 25)
    if is_grote_straat(stenen):
        score = max(score, 40)
    elif is_kleine_straat(stenen):
        score = max(score, 30)
    return score

def is_grote_straat(stenen):
    stenen.sort()
    gstraat = True
    lengte = len(stenen) - 1
    for x in range(lengte):
        if stenen[x] + 1 != stenen[x+1]:
            gstraat = False
    return gstraat
    
def is_kleine_straat(stenen):
    stenen.sort()
    lengte = len(stenen)
    for x in range(lengte):
        kstraat = True
        steen = stenen.copy()
        steen.pop(x)
        lang = len(steen) - 1
        for y in range(lang):
            if steen[y] + 1 != steen[y+1]:
                kstraat = False
        if kstraat:
            return True
    return False