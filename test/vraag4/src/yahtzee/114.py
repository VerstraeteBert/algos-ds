def histogram(l):
    di = {}
    for i in l:
        if i in di:
            di[i] += 1
        else:
            di[i] = 1
    return di

def max_gelijk(l):
    di = histogram(l)
    l = []
    for i in di:
        l.append(di[i])
    return max(l)

def is_FullHouse(l):
    di = histogram(l)
    l = []
    for i in di:
        l.append(di[i])
    if 2 in l and 3 in l:
        return True
    else:
        return False
def is_grote_straat(s):
    s.sort()
    for i in range(1, len(s)-1):
        if (s[i] != s[i-1] + 1):
            return False
    return True

def is_kleine_straat(s):
    s.sort()
    c = 0
    for i in range(5):
        if (s[i] != s[i-1] + 1):
            c += 1
    for i in range(1,6):
        if (s[i] != s[i - 1] + 1):
            c += 1
    if c >= 1:
        return True
    else:
        return False
    
def grootste_score(ll):
    di = histogram(ll)
    l = []
    for i in di:
        l.append(di[i])
    if 2 in l and 3 in l:
        return 25
    elif 5 in l:
        return 50
    elif is_grote_straat(ll) == True:
        return 40
    elif is_kleine_straat(ll) == True:
        return 30
    #kleine straat
    else:
        return sum(ll)

