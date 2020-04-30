def histogram(stenen):
    stenen.sort()
    a = 0
    dictonarie = {}
    for k in range(len(stenen)):
        if k == len(stenen) - 1:
            if stenen[k] != stenen[k-1]:
                dictonarie[stenen[k]] = 1
            else:
                dictonarie[stenen[k]] = k - a + 1
        else:
            if stenen[k] != stenen[k+1]:
                dictonarie[stenen[k]] = k - a + 1
                a = k + 1
    return dictonarie

def max_gelijk(stenen):
    a = 0
    dictonarie = histogram(stenen)
    for steen in dictonarie:
        if dictonarie[steen] > a:
            a = dictonarie[steen]
    return a

def is_FullHouse(stenen):
    output = False
    a = 0
    b = 0
    dictonarie = histogram(stenen)
    for steen in dictonarie:
        if dictonarie[steen] == 2:
            a = 1
        if dictonarie[steen] == 3:
            b = 1
    if a == 1 and b == 1:
        output = True
    return output


def is_kleine_straat(stenen):
    output = False
    stenen.sort()
    a = 0
    lengte = len(stenen)
    for i in range(1,lengte):
        element = stenen[i]
        if element == stenen[i-1] + 1:
            a += 1
            if a >= lengte - 2:
                output = True
        elif element == stenen[i-1]:
            continue
        else:
            a = 0
    return output
def is_grote_straat(stenen):
    stenen.sort()
    a = 0
    lengte = len(stenen)
    for i in range(1,lengte):
        element = stenen[i]
        if element == stenen[i-1] + 1:
            a += 1
    if a == lengte - 1:
        output = True
    else:
        output = False
    return output

def grootste_score(stenen):
    lijst = []
    dictonarie = histogram(stenen)
    for steen in dictonarie:
        if dictonarie[steen] == 3:
            lijst.append(sum(stenen))
        if dictonarie[steen] == 4:
            lijst.append(sum(stenen))
        if dictonarie[steen] == 5:
            lijst.append(50)
    if is_FullHouse(stenen) == True:
        lijst.append(25)
    lijst.append(sum(stenen))
    if is_kleine_straat(stenen) == True:
        lijst.append(30)
    if is_grote_straat(stenen) == True:
        lijst.append(40)
    score = max(lijst)
    return score