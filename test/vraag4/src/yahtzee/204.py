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
                tel = 1  # herbegin telling

    return tel >= len(stenen) - 1

def is_grote_straat(stenen):
    gesorteerde_stenen = sorted(stenen)
    for i in range(1, len(gesorteerde_stenen)):
        if gesorteerde_stenen[i] != gesorteerde_stenen[i - 1] + 1:
            return False
    return True

def is_Yathzee(stenen):
    stenen.sort()
    return stenen[0] == stenen[-1]

def histogram(stenen):
    dictionary = {}
    for cijfer in stenen:
        if cijfer in dictionary:
            dictionary[cijfer] += 1
        else:
            dictionary[cijfer] = 1
    return dictionary

def max_gelijk(stenen):
    tel = 0
    for cijfer in stenen:
        if tel < stenen.count(cijfer):
            tel = stenen.count(cijfer)
    return tel

def is_FullHouse(stenen):
    stenen.sort()
    if stenen.count(stenen[0]) == 3 and stenen.count(stenen[-1]) == 2:
        return True
    if stenen.count(stenen[0]) == 2 and stenen.count(stenen[-1]) == 3:
        return True
    return False

def som(stenen):
    return sum(stenen)

def grootste_score(stenen):
    totaal = som(stenen)
    if max_gelijk(stenen) == 3:
        totaal = som(stenen)
    if max_gelijk(stenen) == 4:
        totaal = som(stenen)
    if is_kleine_straat(stenen):
        if totaal < 30:
            totaal = 30
    if is_grote_straat(stenen):
        if totaal < 40:
            totaal = 40
    if is_FullHouse(stenen):
        if totaal < 25:
            totaal = 25
    if is_Yathzee(stenen):
        if totaal < 50:
            totaal = 50
    return totaal
