def histogram(stenen):
    boekhouding = {}
    for steen in stenen:
        if steen not in boekhouding:
            boekhouding[steen] = 1
        else:
            boekhouding[steen] += 1
    return boekhouding        
            
            
def max_gelijk(stenen):
    return max(histogram(stenen).values())
    
    
def is_FullHouse(stenen):
    boekhouding = histogram(stenen)
    return len(boekhouding) == 2 and 2 in boekhouding.values() and 3 in boekhouding.values() 
    
    
def som(stenen):
    return sum(stenen)

def is_Yathzee(stenen):
    return max(stenen) == min(stenen)

def is_grote_straat(stenen):
    stenen.sort()
    for i in range(len(stenen)-1):
        if stenen[i] + 1 != stenen[i+1]:
            return False
    return True    
    

def is_kleine_straat(stenen): 
    aantal_stenen = len(stenen)
    stenen.sort()
    stenen_uniek = []
    for steen in stenen:
        if not steen in stenen_uniek:
            stenen_uniek.append(steen)
    if len(stenen_uniek) < aantal_stenen - 1: 
        return False
    aantal = 0
    for i in range(len(stenen_uniek)-1):
        if stenen_uniek[i] == stenen_uniek[i+1] - 1:
            aantal += 1
            if aantal >= aantal_stenen - 2:
                return True
        else:
            aantal = 0
    return False


def grootste_score(stenen):
    boekhouding = histogram(stenen)
    scores = []
    if is_Yathzee(stenen):
        scores.append(50)
    elif is_FullHouse(stenen):
        scores.append(25)
    elif is_grote_straat(stenen):
        scores.append(40)
    elif is_kleine_straat(stenen):
        scores.append(30)
    # elif x_of_a_kind(4,stenen) or x_of_a_kind(3,stenen):
    #     scores.append(sum(stenen))
    scores.append(sum(stenen))
    return max(scores)    
        