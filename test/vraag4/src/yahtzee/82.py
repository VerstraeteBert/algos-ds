def som(stenen):
    return sum(stenen)

def is_Yathzee(stenen):
    if stenen.count(stenen[0]) == len(stenen):
        return True
    else:
        return False

def is_grote_straat(stenen):
    stenen.sort()
    for item in stenen:
        if stenen.count(item)>1:
            return False
    if stenen[-1]==(stenen[0]+len(stenen)-1):
        return True
    else:
        return False
    

def is_kleine_straat(stenen):
    lengte = len(stenen)
    stenen.sort()
    for item in stenen:
        if stenen.count(item)>1:
            stenen.remove(item)
    if len(stenen)<lengte-1:
        return False
    elif len(stenen)==lengte:
        nieuw = stenen[1:]
        if is_grote_straat(nieuw):
            return True
        nieuw = stenen[:-1]
        if is_grote_straat(nieuw):
            return True
    else:
        if is_grote_straat(stenen):
            return True
    return False


#----------------------------------------------

def histogram(lijst):
    d={}
    for item in lijst:
        if item in d:
            d[item]+=1
        else:
            d[item]=1
    return d

def max_gelijk(lijst):
    d = histogram(lijst)
    max=0
    for item in d:
        if d[item]>max:
            max = d[item]
    return max


def is_FullHouse(lijst):
    d = histogram(lijst)
    twee = []
    for x,y in d.items():
        twee.append(y)
    if 2 in twee and 3 in twee:
        return True
    return False

from copy import deepcopy

def grootste_score(lijst):
    scores = []
    scores.append(som(lijst))
    if max_gelijk(lijst) == 5:
        scores.append(50)
    if is_grote_straat(lijst):
        scores.append(40)
    lijst2=deepcopy(lijst)
    if is_kleine_straat(lijst2):
        scores.append(30)
    if is_FullHouse(lijst):
        scores.append(25)
    return max(scores)