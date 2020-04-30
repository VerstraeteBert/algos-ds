def histogram(stenen):
    dictionary = {}
    stenen.sort()
    for i in range(1, 2000):
        aantal = stenen.count(i)
        if aantal != 0:
            dictionary[i] = aantal
    return dictionary

def max_gelijk(stenen):
    max_aantal = 0
    for i in range(1, 2000):
        aantal = stenen.count(i)
        if aantal > max_aantal:
            max_aantal = aantal
    return max_aantal

def is_FullHouse(stenen):
    a = 0
    b = 0
    for i in range(1, 7):
        aantal = stenen.count(i)
        if aantal == 2:
            a = 1
        if aantal == 3:
            b = 1
    if a == 1 and b == 1:
        value = True
    else:
        value = False
    return value

def grootste_score(stenen):
    grootste_score = 0
    aantal = 0
    stenen.sort()
    for q in range(len(stenen)-1):
        if (stenen[q]+1) == stenen[q+1]:
            aantal += 1
    if aantal == len(stenen)-1:
        if 40 > grootste_score:
            grootste_score = 40

    aantal = 0
    for s in range(len(stenen) - 1):
        if stenen[s] == stenen[s + 1]:
            aantal += 1
    if aantal == len(stenen) - 1:
        if 50 > grootste_score:
            grootste_score = 50

    aantal1 = 0
    aantal2 = 0
    aantal3 = 0
    aantal4 = 0
    stenen.sort()
    stenen2 = []
    for m in range(len(stenen) - 1):
        if stenen[m] != stenen[m + 1]:
            stenen2.append(stenen[m])
    stenen2.append(stenen[m + 1])
    if len(stenen2) != (len(stenen) - 1):
        stenen2 = ''
    for i in range(len(stenen) - 2):
        if (stenen[i] + 1) == stenen[i + 1]:
            aantal1 += 1
    for k in range(1, len(stenen) - 1):
        if (stenen[k] + 1) == stenen[k + 1]:
            aantal2 += 1
    for m in range(len(stenen) - 1):
        if (stenen[m] + 1) == stenen[m + 1]:
            aantal3 += 1
    for a in range(len(stenen2) - 1):
        if (stenen2[a] + 1) == stenen2[a + 1]:
            aantal4 += 1
    if ((aantal1 == len(stenen) - 2 or aantal2 == len(stenen) - 2 or aantal3 == len(stenen) - 1)) or aantal4 == len(stenen) - 2:
        if 30 > grootste_score:
            grootste_score = 30
    a = 0
    b = 0
    for h in range(1, 2000):
        aantal = stenen.count(h)
        if aantal == 2:
            a = 1
        if aantal == 3:
            b = 1
    if a == 1 and b == 1:
        if 25 > grootste_score:
            grootste_score = 25

    som = sum(stenen)
    if som > grootste_score:
        grootste_score = som

    return grootste_score