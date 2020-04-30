def som(stenen):
    return sum(stenen)


def is_Yathzee(stenen):
    return 1 == len(set(stenen))


def is_grote_straat(stenen):
    if max(stenen) == min(stenen)+len(stenen)-1 and len(set(stenen)) == len(stenen):
        return True
    return False


def is_kleine_straat(stenen):
    max1 = stenen[:]
    min1 = stenen[:]
    max1.remove(max(stenen))
    min1.remove(min(stenen))
    midden = set(stenen)
    if max(max1) == min(max1)+len(max1)-1 and len(set(max1)) == len(max1):
        return True
    if max(min1) == min(min1)+len(min1)-1 and len(set(min1)) == len(min1):
        return True
    if max(midden) == min(midden) + len(midden) - 1 and len(midden) == len(stenen)-1:
        return True
    return False
    
from collections import Counter

def histogram(stenen):
    list(stenen).sort()
    bib = Counter(stenen)
    return dict(bib)

def max_gelijk(stenen):
    dict = histogram(stenen)
    max = 0
    for i in dict:
        if int(dict[i])> max:
            max = dict[i]
    return max

def is_FullHouse(stenen):
    if len(set(stenen))==2 and min(histogram(stenen).values()) > 1 :
        return True
    return False
    
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
            
