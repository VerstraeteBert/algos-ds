def som(stenen):
    som = int(sum(stenen))
    return som


def is_Yathzee(stenen):
    getal = int(stenen[0])
    yathzee = False
    for i in stenen:
        if i == getal:
            yathzee = True
        else:
            yathzee = False
            break
    return yathzee


def is_grote_straat(stenen):
    stenen.sort()
    start = 1
    noof_op_volgorde = 1
    max_noof_op_volgorde = 0
    prev_val = 0
    for steen in stenen:
        if start == 1:
            prev_val = steen
            start = 0
        else:
            if prev_val == (steen-1):
                noof_op_volgorde += 1
                if noof_op_volgorde > max_noof_op_volgorde:
                    max_noof_op_volgorde = noof_op_volgorde
            else:
                noof_op_volgorde = 1
            prev_val = steen
    if max_noof_op_volgorde == 5:
        return True
    else:
        return False



    if int(stenen[-2]) == int(stenen[-1])-1:
        gstraat = True
    else:
        gstraat = False
    i = 0
    while i < len(stenen)-1:
        if int(stenen[i]) == int(stenen[i+1])-1:
            gstraat = True
            i += 1
        else:
            gstraat = False
            break
    return gstraat


def is_kleine_straat(stenen):
    stenen.sort()
    stenen_2 = stenen[:]

    start = 1
    noof_op_volgorde = 1
    max_noof_op_volgorde = 0
    prev_val = 0
    for steen in stenen:
        if start == 1:
            prev_val = steen
            start = 0
        else:
            if prev_val == (steen-1):
                noof_op_volgorde += 1
                if noof_op_volgorde > max_noof_op_volgorde:
                    max_noof_op_volgorde = noof_op_volgorde
            elif prev_val != steen:
                noof_op_volgorde = 1
            prev_val = steen
    if max_noof_op_volgorde == 4:
        return True
    else:
        return False

    getal = int(stenen[0])
    yathzee = False
    for i in stenen:
        if i == getal:
            yathzee = True
        else:
            yathzee = False
            break
    if False:
    #yathzee == True:
        kstraat = False
    else:
        i = 0
        while i < len(stenen) - 1:
            if int(stenen[i]) == int(stenen[i + 1]):
                stenen.remove(stenen[i])
                i = 0
            else:
                i += 1
        if int(stenen[-2]) == int(stenen[-1]):
            stenen.remove(stenen[-1])

        if len(stenen_2)-1 == len(stenen) or len(stenen_2) == len(stenen):
            a = 0
            if int(stenen[-2]) == int(stenen[-1])-1:
                kstraat = True
            else:
                kstraat = False
            while a < len(stenen) - 1:
                if int(stenen[a]) == int(stenen[a + 1]) - 1:
                    kstraat = True
                    a += 1
                else:
                    kstraat = False
                    break
        else:
            kstraat = False
    return kstraat

def histogram(stenen):
    hist = {}
    for steen in stenen:
        if steen in hist:
           hist[steen] += 1
        else:
           hist[steen] = 1

    return hist

def max_gelijk(stenen):
    hist = histogram(stenen)
    current = 0
    for h in hist:
        if hist[h] > current:
            current = hist[h]
    return current

def is_FullHouse(stenen):
    gelijke = max_gelijk(stenen)
    if gelijke == 5:
        return False
    if gelijke == 3:
        hist = histogram(stenen)
        if len(hist) == 2:
            return True
    return False

def grootste_score(stenen):
    hist = histogram(stenen)
    gelijke = max_gelijk(stenen)
    score = 0
    max_score = som(stenen)
    if gelijke == 3:
        score = som(stenen)
        max_score = score
    if gelijke == 4:
        score = som(stenen)
        if max_score < score:
            max_score = score
    if is_grote_straat(stenen):
        score = 40
        if max_score < score:
            max_score = score
    if is_FullHouse(stenen):
        score = 25
        if max_score < score:
            max_score = score
    if is_Yathzee(stenen):
        score = 50
        if max_score < score:
            max_score = score
    if is_kleine_straat(stenen):
        score = 30
        if max_score < score:
            max_score = score
    return max_score
