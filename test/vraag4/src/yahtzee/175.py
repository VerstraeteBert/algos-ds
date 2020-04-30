def som(inp):
    return sum(inp)

def is_Yathzee(inp):
    return min(inp) == max(inp)

def is_grote_straat(inp):
    inp.sort()
    for i in range(1, len(inp)):
        if inp[i-1] != inp[i] - 1:
            return False
    return True

def is_kleine_straat(inp):
    inp.sort()
    inp_uniek = list(set(inp))
    teller = 1
    for i in range(1, len(inp_uniek)):
        if inp_uniek[i - 1] == inp_uniek[i] - 1:
            teller += 1
        elif i not in (1, len(inp_uniek) - 1):
            return False
    return teller >= len(inp) - 1

def histogram(inp):
    inp.sort()
    inp_uniek = list(set(inp))
    d = {}
    for i in inp_uniek:
        d[i] = inp.count(i)
    return d

def max_gelijk(inp):
    d = histogram(inp)
    return max(d.values())

def min_gelijk(inp):
    d = histogram(inp)
    return min(d.values())

def is_FullHouse(inp):
    return max_gelijk(inp) == 3 and min_gelijk(inp) == 2

def grootste_score(inp):
    if is_Yathzee(inp):
        return 50
    elif is_grote_straat(inp):
        return 40
    elif is_kleine_straat(inp):
        return 30
    else:
        scores = []
        if is_FullHouse(inp):
            scores.append(25)
        scores.append(som(inp))
        return max(scores)