def histogram(l):
    l.sort()
    woordenboek = {}
    for i in l:
        if i not in woordenboek:
            woordenboek[i] = l.count(i)
    return woordenboek

def max_gelijk(l):
    maximaal = 0
    for i in l:
        aantal = l.count(i)
        if aantal > maximaal:
            maximaal = aantal
    return maximaal

def is_FullHouse(l):
    getallen = []
    for i in l:
        if i not in getallen:
            getallen.append(i)
    if len(getallen) != 2:
        return False
    else:
        if l.count(getallen[0]) == 3 and l.count(getallen[1]) == 2 or l.count(getallen[0]) == 2 and l.count(getallen[1]) == 3:
            return True
        else: 
            return False

def grootste_score(l):
    maximum = 0
    optel = sum(l)
    for i in l:
        aantal = l.count(i)
        waarde = i*aantal
        if waarde > maximum:
            maximum = waarde
        if l.count(i) == 5:
            maximum = 50
        if is_FullHouse(l) == True:
            Full = 25
            if Full > maximum:
                maximum = Full
        if l.count(i) == 3 or l.count(i) == 4:
            som = sum(l)
            if som > maximum:
                maximum = som
        if optel > maximum:
            maximum = sum(l)
    l.sort()
    correct = 0
    for i in range(len(l)):
        if l[i] - l[0] == i:
            correct += 1
    if correct == 5:
        if 40 > maximum:
            maximum = 40
    nieuw = []
    for cijfer in l:
        if cijfer not in nieuw:
            nieuw.append(cijfer)
    correct1 = 0
    correct2 = 0
    for i in range(len(nieuw)):
        if nieuw[i] - nieuw[0] == i:
            correct1 += 1
    for e in range(len(nieuw)-1):
        if nieuw[e+1] - nieuw[1] == e:
            correct2 += 1
    if correct1 >= len(l)-1:
        klein = 30
    elif correct2 >= len(l)-1:
        klein = 30
    try:
        if klein > maximum:
            maximum = klein
    except UnboundLocalError:
        pass
    return maximum  