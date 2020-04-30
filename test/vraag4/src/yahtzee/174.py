def histogram(stenen):
    result = {}
    for i in stenen:
        if i in result.keys():
            result[i] += 1
        else:
            result.update({i: 1})
    return result
    
def max_gelijk(stenen):
    stenen.sort()
    count = 1
    result = []
    for i in range(len(stenen)-1):
        if stenen[i] == stenen[i + 1]:
            count += 1
        else:
            result.append(count)
            count = 1
    result.append(count)
    result.sort()
    return result[-1]

def is_FullHouse(stenen):
    stenen.sort()
    i = stenen
    if (i[0] == i[1] == i[2] and i[3] == i[4]):
        return True
    elif i[2] == i[3] == i[4] and i[0] == i[1]:
        return True
    return False

def grootste_score(stenen):
    stenen.sort()
    #if max_gelijk(stenen) >= 3:
    #    return sum(stenen)
    if stenen[0] == stenen[1] - 1 == stenen[2] - 2 == stenen[3] - 3 == stenen[4] - 4:
        return 40
    elif is_FullHouse(stenen):
        return 25
    elif stenen[0] == sum(stenen)/len(stenen):
        return 50
    else:
        newstenen = stenen.copy()
        for i in range(len(stenen)-1):
            if stenen[i] == stenen[i+1]:
                del newstenen[i]
                break
        if newstenen[0] == newstenen[1] - 1 == newstenen[2] - 2 == newstenen[3] - 3:
            return 30
        return sum(stenen)