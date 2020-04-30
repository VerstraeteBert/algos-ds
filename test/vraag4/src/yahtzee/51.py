def histogram(stenen):
    myDictionary = {}
    myList = sorted(stenen)
    val = 0
    i = 1
    while i <= len(myList):
        a = myList[i-1]
        key = a

        if key in myDictionary:
            val = myDictionary[key]
            val += 1
            myDictionary[key] = val

        else:
            myDictionary[key] = 1
        i += 1

    return myDictionary

def max_gelijk(stenen):
    maxg = histogram(stenen)
    max = 0
    for key in maxg.values():
        if key > max:
            max = key


    return max

def is_FullHouse(stenen):
    fullh = histogram(stenen)
    ok = False
    if len(fullh) == 2:
        for key in fullh.values():
            if key == 3:
                ok = True
    else:
        ok = False
    return ok

def grootste_score(stenen):
    fullh = histogram(stenen)
    sorted(fullh)
    ok = False
    hoog = 0
    #check voor 3 dezelfde
    if len(fullh) == 3:
        for key in fullh:
            hoog += (fullh[key] * key)

    if len(fullh) == 2:
        check = 0
        controleer = 0
        tot = 1
        geenFH = False
        for key in fullh:
            check += fullh[key] * key
            if fullh[key] > 3:
               geenFH = True
        if check < 25 and geenFH == False:
            check = 25  # value van kleine straat
        if check > hoog:
            hoog = check

    if len(fullh) == 1:
        hoog = 50

    if len(fullh) == 4:
        check = 0
        controleer = 0
        tot = 1
        for key in fullh:
            check += fullh[key] * key
            if controleer == 0:
                controleer = key

            else:
                b = key
                if controleer + 1 == b:
                    controleer = b
                    tot += 1
                else:
                    tot = 0
        if check < 30 and tot == 4:
            check = 30 #value van kleine straat
        if check > hoog:
            hoog = check
    if len(fullh) == 5:
        check = 0
        controleer = 0
        tot = 1
        for key in fullh:
            check += fullh[key] * key
            if controleer == 0:
                controleer = key
            else:
                b = key

                if controleer + 1 == b:

                    controleer = b
                    tot += 1

                else:
                    controleer = b
                    if tot < 4:
                        tot = 1


        if check < 40 and tot == 5:
            check = 40 #value van grote straat

        if check < 30 and tot == 4:
            check = 30
        if check > hoog:
            hoog = check
    return hoog

