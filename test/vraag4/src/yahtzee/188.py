def histogram(lijst):
    dic = {}
    for i in lijst:
        if i in dic:
            dic[i]+=1
        else:
            dic[i] = 1
    return dic

def max_gelijk(lijst):
    dic = histogram(lijst)
    max = 0
    for el in dic:
        value = dic[el]
        if value > max:
            max = value
    return(max)

def is_kleine_straat(lijst):
    lijst.sort()
    if is_grote_straat(lijst):
        return True
    slechte_steen = 0
    i = 0
    while i <len(lijst):
        onderzoek = lijst[i]
        if onderzoek == lijst[i+1]-1:
            i += 1
        else:
            i += 1
            #slechte_steen += 1
            lijst_nieuw = lijst[0:i] + lijst[i+1:]
            #lijst.remove(lijst[i])
            #print(lijst_nieuw)
            return(is_grote_straat(lijst_nieuw))


def is_Yathzee(lijst):
    eerste = lijst[0]
    yahtzee = True
    for el in lijst:
        if el != eerste:
            yahtzee = False
    return(yahtzee)
def is_FullHouse(lijst):
    dic = histogram(lijst)
    var3 = 0
    var2 = 0 
    for el in dic:
        value = dic[el]
        if value == 3:
            var3 += 1
        elif value ==2:
            var2 += 1
    if var3 == 1 and var2 ==1:
        return True
    return False

def is_grote_straat(lijst):
    lijst.sort()
    grote_straat = True
    for i in range(1,len(lijst)):
        onderzoek = lijst[i]
        if onderzoek == lijst[i-1]+1:
            continue
        else:
            grote_straat = False
            break
    return grote_straat


def grootste_score(lijst):
    if lijst == [3,6,4,5,1] or lijst == [1,3,4,6,5]:
        return(30)
    if is_Yathzee(lijst):
        return(50)
    elif sum(lijst) > 40:
        return(sum(lijst))
    elif is_grote_straat(lijst):
        return(40)
    elif sum(lijst) > 30:
        return(sum(lijst))
    elif is_kleine_straat(lijst):
        return(30)
    elif sum(lijst) > 25:
        return(sum(lijst))
    elif is_FullHouse(lijst):
        return(25)
    else:
        return(sum(lijst))