def is_grote_straat(stenen):
    worpen = sorted(stenen)
    for pos in range(1,len(worpen)):
        if worpen[pos] != worpen[pos-1]+1:
            return False
    return True

def is_kleine_straat(stenen):
    opeenvolgend = 1
    worpen = sorted(stenen)
    for pos in range(1, len(worpen)):
        if worpen[pos] == worpen[pos-1]+1:
            opeenvolgend += 1
        elif opeenvolgend < len(stenen)-1 and worpen[pos] != worpen[pos-1]:
            opeenvolgend = 1
    if opeenvolgend >= len(stenen)-1:
        return True
    else:
        return False

def histogram(stenen):
    boek = {}
    for steen in sorted(stenen):
        if steen not in boek.keys():
            boek[steen] = 1
        else:
            boek[steen] += 1
    return boek

def max_gelijk(stenen):
    boek = histogram(stenen)
    return max(boek.values())

def is_FullHouse(stenen):
    boek = histogram(stenen)
    return sorted(boek.values()) == [2,3]

def grootste_score(stenen):
    boek = histogram(stenen)
    grootst = 0
    if 5 in boek.values():
        grootst = 50
    elif is_grote_straat(stenen):
        grootst = max(grootst, 40)
    elif is_kleine_straat(stenen):
        grootst = max(grootst, 30)
    elif is_FullHouse(stenen):
        grootst = max(grootst, 25)
    waarde = sum(stenen)
    grootst = max(grootst, waarde)
    return grootst