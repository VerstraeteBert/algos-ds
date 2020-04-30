def som(stenen):
    return sum(stenen)

def is_Yathzee(stenen):
    return stenen == [stenen[0]]*len(stenen)

def is_grote_straat(stenen):
    '''alle stenen (n) liggen opeenvolgend'''
    stenen = sorted(stenen) #werken met een kopie want er is niet geweten dat we de originele lijst mogen aanpassen
    for i in range(len(stenen)-1):
        if stenen[i] != stenen[i+1]-1:
            return False
    return True

def is_kleine_straat(stenen):
    ''' n-1 stenen liggen opeenvolgend'''
    for i in range(len(stenen)):
        stenen_min_een = stenen[:i] + stenen[i+1:]
        if is_grote_straat(stenen_min_een):
            return True
    return False


def histogram(stenen):
    histogram = {}
    for steen in stenen:
        if steen in histogram:
            histogram[steen] += 1
        else:
            histogram[steen] = 1
    return histogram

def max_gelijk(stenen):
    histogr = histogram(stenen)
    waarden = histogr.values()
    return max(waarden)


def is_FullHouse(stenen):
    histogr = histogram(stenen)
    return len(histogr) == 2 and (3 in histogr.values())

def grootste_score(stenen):
    score = 0
    if is_Yathzee(stenen):
        return 50
    elif is_grote_straat(stenen):
        return 40
    elif is_kleine_straat(stenen):
        return 30
    elif is_FullHouse(stenen):
        score = 25
        
    totaal_ogen = sum(stenen)
    if totaal_ogen > score:
        score = totaal_ogen
    return score