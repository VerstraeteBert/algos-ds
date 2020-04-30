def som(stenen):
    som = sum(stenen)
    return som

def is_Yathzee(stenen):
    lengte = len(stenen)
    controle = stenen[0]
    antwoord = True
    for i in range(lengte):
        if stenen[i] != controle:
            return False
    return antwoord

def is_grote_straat(stenen):
    lengte = len(stenen)
    stenen_sorted = sorted(stenen)
    antwoord = True
    for i in range(lengte-1):
        if stenen_sorted[i] != (stenen_sorted[i+1]-1):
            return False
    return antwoord

def is_kleine_straat(stenen):
    gesorteerde_stenen = sorted(stenen)
    tel = 1
    for i in range(1, len(gesorteerde_stenen)):
        if gesorteerde_stenen[i] == gesorteerde_stenen[i - 1] + 1:
            tel += 1
        else:
            if tel >= len(gesorteerde_stenen) - 1:
                return True
            if gesorteerde_stenen[i] != gesorteerde_stenen[i - 1]:
                tel = 1  

    return tel >= len(stenen) - 1

def histogram(stenen):
    dictionary = {}
    for element in stenen:
        if element not in dictionary:
            dictionary[element] = 1
        elif element in dictionary:
            dictionary[element] += 1
    return dictionary

def max_gelijk(stenen):
    dictionary = histogram(stenen)
    maximum = max(dictionary.values())
    return maximum

def is_FullHouse(stenen):
    fullhouse = False
    histo = histogram(stenen)
    if len(histo) == 2 and min(histo.values()) > 1:
        fullhouse = True
    return fullhouse

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