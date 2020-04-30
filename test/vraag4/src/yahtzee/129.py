def histogram(stenen):
    stenen.sort()
    dictionary = {}
    for item in stenen:
        aantal = 0
        if item in dictionary:
            aantal = dictionary[item]
        dictionary[item] = aantal + 1
    return dictionary


def  max_gelijk(stenen):
    dictionary = histogram(stenen)
    hoogste_aantal = 0
    for item in dictionary:
        if dictionary[item] > hoogste_aantal:
            hoogste_aantal = dictionary[item]
    return hoogste_aantal


def is_FullHouse(stenen):   #enkel 5
    stenen.sort()
    eerste = 0
    aantal_verschillende = 0
    for item in stenen:
        if int(item) != eerste:
            eerste = item
            aantal_verschillende += 1
    if aantal_verschillende != 2:
        return False
    if 3 == max_gelijk(stenen):
        return True
    return False


def is_grote_straat(lijst):
    lijst.sort()
    aantal = 0
    for i in range(len(lijst)-1):
        if int(lijst[i])+1 == int(lijst[i+1]):
            aantal += 1
    if aantal == len(lijst)-1:
        return True
    return False


def is_kleine_straat(lijst):
    aantal = 0
    lengte = len(lijst)
    for i in range(lengte):
        lijst2 = lijst[:i] + lijst[i+1:]
        if is_grote_straat(lijst2):
            aantal += 1
    if aantal > 0:
        return True
    return False


def grootste_score(stenen):
    if max_gelijk(stenen) == 5:
        return 50
    if is_grote_straat(stenen):
        return 40
    if is_kleine_straat(stenen):
        return 30
    if is_FullHouse(stenen) and sum(stenen) < 25:
        return 25
    return sum(stenen)

