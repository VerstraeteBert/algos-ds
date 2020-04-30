def histogram(stenen):
    dictionary = {}
    stenen.sort()
    for waarde in stenen:
        if waarde in dictionary:
            dictionary[waarde] += 1
        else:
            dictionary[waarde] = 1
    return dictionary

def max_gelijk(stenen):
    dictionary = histogram(stenen)
    grootste = 0
    for waarde in dictionary.values():
        if waarde > grootste:
            grootste = waarde
    return grootste

def som(lijst):
    return sum(lijst)

def is_Yathzee(lijst):
    count = 0
    for i in range(len(lijst)-1):
        if lijst[i] == lijst[i+1]:
            count = count
        else:
            count = count + 1
    if count == 0:
        return True
    else:
        return False

def is_grote_straat(lijst):
    lijst.sort()
    count = 0
    for i in range(len(lijst)-1):
        if lijst[i] == lijst[i+1]-1:
            count = count
        else:
            count = count +1
    if count == 0:
        return True
    else:
        return False

def is_kleine_straat(lijst):
    lijst.sort()
    a = 0
    b = -1
    for i in range(len(lijst)-1):
        if lijst[i] == lijst[i+1]:
            b = i
    if b == -1:
        if is_grote_straat(lijst[1:]) == True:
            a = 1
        if is_grote_straat(lijst[:len(lijst) - 1]) == True:
            a = 1
    else:
        del lijst[b]
        if is_grote_straat(lijst) == True:
            a = 1
    if a == 1:
        return True
    else:
        return False


def is_FullHouse(stenen):
    dictionary = histogram(stenen)
    return len(dictionary) == 2 and max_gelijk(stenen) == 3

def grootste_score(stenen):
    lijst = stenen.copy()
    som = 0
    for i in lijst:
        som += i
    if is_Yathzee(stenen) == True and som < 50:
        return 50
    if is_FullHouse(stenen) == True and som < 25:
        return 25
    if is_grote_straat(stenen) == True and som < 40:
        return 40
    if is_kleine_straat(stenen) == True and som < 30:
        return 30
    return som