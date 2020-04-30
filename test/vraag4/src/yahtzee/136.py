def is_Yathzee(stenen):
    cijfer = stenen[0]
    gelijk = False
    for i in range(1,len(stenen)):
        if cijfer == stenen[i]:
            gelijk = True
        else:
            return False
    return True

def is_grote_straat(stenen):
    gesorteerde_stenen = sorted(stenen)
    for i in range(1, len(gesorteerde_stenen)):
        if gesorteerde_stenen[i] != gesorteerde_stenen[i - 1] + 1:
            return False
    return True


def is_kleine_straat(stenen):
    for steen in stenen:
        controle = stenen[:]
        controle.remove(steen)
        if is_grote_straat(controle):
            return True
    return False


def histogram(stenen):  # stenen is een list met alle waarden vd dobbelstenen, ook meerdere dobbelstenen
    woordenboek = {}
    for getal in stenen:
        if getal in woordenboek:
            woordenboek[getal] += 1
        else:
            woordenboek[getal] = 1
    return woordenboek

def max_gelijk(stenen):
    woordenboek = histogram(stenen) #3:9    2:4     5:2
    grootste_cijfer_voorkomt = max(stenen)  #5
    grootste = woordenboek[grootste_cijfer_voorkomt]     #2
    for i in range(1, grootste_cijfer_voorkomt+1):
        if (i in woordenboek) and (woordenboek[i] > grootste):       #Wat als het getal er niet inzit? --> crasht
            grootste = woordenboek[i]
    return grootste


def is_FullHouse(stenen): #enkel met 5 dobbelstenen
    #3 gelijke en één paar. (5 gelijke telt niet als Full House, tenzij het vak Yahtzee reeds ingevuld is).
    driegelijk = False
    tweegelijk = False
    woordenboek = histogram(stenen)
    maximum = max(stenen)
    grootste = max_gelijk(stenen)
    if grootste < 3:
        return False
    else:
        for i in range(0,maximum+1):   #niet lengte nemen van woordenboek, maar grootste dat voorkomt in woordenboek
            if i in woordenboek:
                if woordenboek[i] == 3:             #als het niet voorkomt?
                    driegelijk = True
                elif woordenboek[i] == 2:
                    tweegelijk = True
                elif woordenboek[i] == 5:
                    return False
    if driegelijk and tweegelijk:
        return True
    return False


def grootste_score(stenen):
    score = 0
    if is_Yathzee(stenen):
        score += 50
    elif is_grote_straat(stenen):
        score = 40
    elif is_kleine_straat(stenen):
        score = 30
    elif is_FullHouse(stenen):
        score = 25

    totaal_ogen = sum(stenen)
    if totaal_ogen > score:
        score = totaal_ogen
    return score
