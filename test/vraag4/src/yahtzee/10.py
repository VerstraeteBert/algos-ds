def histogram(stenen):
    dictionary = {}
    for cijfer in stenen:
        if cijfer in dictionary:
            dictionary[cijfer] += 1
        else:
            dictionary[cijfer] = 1
    return dictionary
    
def max_gelijk(stenen):
    dictionary = histogram(stenen)
    return max(dictionary.values())
    
def is_FullHouse(stenen):
    dictionary = histogram(stenen)
    if max(dictionary.values()) == 3 and min(dictionary.values()) == 2:
        return True
    else:
        return False

def som(lijst):
    return sum(lijst)


def is_Yathzee(lijst):
    gesorteerde_stenen = sorted(lijst)
    return gesorteerde_stenen[0] == gesorteerde_stenen[-1]


def is_grote_straat(lijst):
    gesorteerde_stenen = sorted(lijst)
    for i in range(1, len(gesorteerde_stenen)):
        if gesorteerde_stenen[i] != gesorteerde_stenen[i - 1] + 1:
            return False
    return True


def is_kleine_straat(lijst):
    gesorteerde_stenen = sorted(lijst)
    tel = 1
    for i in range(1, len(gesorteerde_stenen)):
        if gesorteerde_stenen[i] == gesorteerde_stenen[i - 1] + 1:
            tel += 1
        else:
            if tel >= len(gesorteerde_stenen) - 1:
                return True
            if gesorteerde_stenen[i] != gesorteerde_stenen[i - 1]:
                tel = 1

    return tel >= len(lijst) - 1

def grootste_score(stenen):
    punten = 0
    uitzondering = 0
    if is_Yathzee(stenen):
        punten += 50
    elif is_grote_straat(stenen):
        punten += 40
    elif is_kleine_straat(stenen):
        punten += 30
    elif is_FullHouse(stenen):
        punten += 25
    for cijfer in stenen:
        uitzondering += cijfer
    if punten < uitzondering:
        punten = uitzondering
    return punten