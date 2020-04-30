def som(a):
    return sum(a)

def is_Yathzee(a):
    for i in a:
        if a.count(i) == len(a):
            return True
        else:
            return False

def is_grote_straat(a):
    b = sorted(a)
    c = 0
    for i in range(0, len(a)-1):
        if b[i] == b[i + 1] - 1:
            c += 1
    if c == len(a)-1:
        return True
    else:
        return False

def is_kleine_straat(a):
    b = sorted(a)
    c = 1
    for i in range(1, len(a)):
        if b[i] == b[i - 1] + 1:
            c += 1
        else:
            if c >= len(a) - 1:
                return True
            if b[i] != b[i - 1]:
                c = 1
    if c >= len(a) - 1:
                return True

def histogram(lijst):
    a = {}
    for i in range(1,11):
        if i in lijst:
            a[i] = lijst.count(i)
    return a
        
def max_gelijk(lijst):
    a = 0
    for i in range(1,11):
        b = lijst.count(i)
        if b > a:
            a = b
    return a

def is_FullHouse(lijst):
    a = 0
    b = 0
    for i in range(1,11):
        if lijst.count(i) == 2:
            a += i
        if lijst.count(i) == 3:
            b += i
    if a != 0 and b!= 0:
        return True
    else:
        return False
def grootste_score(lijst):
    a = 0
    if is_Yathzee(lijst):
        a = 50
    elif is_grote_straat(lijst):
        a = 40
    elif is_kleine_straat(lijst):
        a = 30
    elif is_FullHouse(lijst):
        a = 25
        
    b = sum(lijst)
    if b > a:
        a = b
    return a
