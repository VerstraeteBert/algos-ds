def som(stenen):
    return sum(stenen)

def is_Yathzee(stenen):
    return min(stenen) == max(stenen)

def is_grote_straat(stenen):
    gesorteerde_stenen = sorted(stenen)
    i = 0
    while (i < len(gesorteerde_stenen) - 1) and (gesorteerde_stenen[i] + 1 == gesorteerde_stenen[i+1]):
        i += 1
    return i == len(gesorteerde_stenen) - 1
    
def is_kleine_straat(stenen):
    gesorteerde_stenen = sorted(stenen)
    i = 0
    aantal_opeenvolgend = 1
    while i < len(gesorteerde_stenen) - 1 and aantal_opeenvolgend < len(gesorteerde_stenen) - 1:
        if gesorteerde_stenen[i] + 1 == gesorteerde_stenen[i+1]:
            aantal_opeenvolgend += 1
        elif gesorteerde_stenen[i] != gesorteerde_stenen[i+1]:
            aantal_opeenvolgend = 1 #herbegin telling
        i += 1
    return aantal_opeenvolgend >= len(gesorteerde_stenen) - 1
    
def histogram(stenen):
    frequentie = {}
    for steen in stenen:
        if steen in frequentie:
            frequentie[steen] += 1
        else:
            frequentie[steen] = 1
    return frequentie

def max_gelijk(stenen):
    frequentie = histogram(stenen)
    aantallen = list(frequentie.values())
    return max(aantallen)
    
def is_FullHouse(stenen):
    gesorteerd = sorted(stenen)
    return (stenen.count(gesorteerd[0]) == 2 and stenen.count(gesorteerd[-1]) == 3) or (stenen.count(gesorteerd[0]) == 3 and stenen.count(gesorteerd[-1]) == 2)
    
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
            