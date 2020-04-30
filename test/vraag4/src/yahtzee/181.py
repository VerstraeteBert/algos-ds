def som(l):
    som = 0
    for element in l:
        som += element
    return som

def is_Yathzee(l):
    for element in l:
        if element != l[0]:
            return False
    return True

def is_grote_straat(l):
    l = sorted(l)
    for i in range(1, len(l) - 1):
        if not (l[i] == l[i - 1] + 1 and l[i] == l[i + 1] - 1):
            return False
    return True

def is_kleine_straat(l):
    l = sorted(l)
    if is_grote_straat(l[1:]) or is_grote_straat(l[:-1]):
        return True
    if len(dubbel(l)) == len(l) -1:
        if is_grote_straat(dubbel(l)):
            return True
    return False
    
def dubbel(l):
    getallen = []
    for i in l:
        if i not in getallen:
            getallen += [i, ]
    return getallen

def histogram(stenen):
    d = {}
    for element in stenen:
        if element not in d:
            d[element] = 0
        d[element] += 1
    return d

def max_gelijk(stenen):
    d = histogram(stenen)
    maximum = 0
    for i in d:
        if d[i] > maximum:
            maximum = d[i]
    return maximum

def is_FullHouse(stenen):
    d = histogram(stenen)
    if len(d) == 2:
        for i in d:
            if d[i] != 2 and d[i] != 3:
                return False
            return True
    return False
    
def grootste_score(stenen):
    scores = []
    d = histogram(stenen)
    if is_FullHouse(stenen):
        scores += [25, ]
    elif is_grote_straat(stenen):
        scores += [40, ]
    elif is_Yathzee(stenen):
        scores += [50, ]
    elif is_kleine_straat(stenen):
        scores += [30, ]
    grootste_aantal = max_gelijk(stenen)
    for i in d:
        if d[i] == grootste_aantal:
            scores += [i*grootste_aantal, ]
    scores += [som(stenen), ]
    return max(scores)