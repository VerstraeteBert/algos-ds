def som(stenen):
    return sum(stenen)

def is_Yathzee(stenen):
    gesorteerde_stenen = sorted(stenen)
    return gesorteerde_stenen[0] == gesorteerde_stenen[-1]

def is_grote_straat(stenen):
    gesorteerde_stenen = sorted(stenen)
    for i in range(1, len(gesorteerde_stenen)):
        if gesorteerde_stenen[i] != gesorteerde_stenen[i - 1] + 1:
            return False
    return True

def is_kleine_straat(stenen):
    gesorteerde_stenen = sorted(stenen)
    tel = 1
    for i in range(1, len(gesorteerde_stenen)):
        if gesorteerde_stenen[i] == gesorteerde_stenen[i - 1] + 1:
            tel += 1
        else:
            if tel >= len(gesorteerde_stenen) - 1:
                return True
            if gesorteerde_stenen[i] != gesorteerde_stenen[i - 1]:
                tel = 1  # herbegin telling

    return tel >= len(stenen) - 1

def histogram(lijst):
    verzameling = {}
    lijst.sort()
    for teller in range(0,len(lijst)):
        waarde = lijst[teller]

        if waarde in verzameling:
            reserve = verzameling[waarde]
            reserve += 1
            verzameling[waarde] = reserve

        else:
            verzameling[waarde] = 1
    return verzameling

def max_gelijk(lijst):
    verzameling = histogram(lijst)
    return max(verzameling.values())

def is_FullHouse(lijst):
    verzameling = histogram(lijst)
    if len(verzameling) == 2:
        getal1, getal2 = verzameling.values()

        if (getal1 == 2) and (getal2 == 3):
            return True
        elif (getal1 == 3) and (getal2 == 2):
            return True
        else:
            return False

    else:
        return False

def grootste_score(lijst):
    score = 0
    if is_Yathzee(lijst):
        score = 50
    elif is_grote_straat(lijst):
        score = 40
    elif is_kleine_straat(lijst):
        score = 30
    elif is_FullHouse(lijst):
        score = 25

    totaal_ogen = sum(lijst)
    if totaal_ogen > score:
        score = totaal_ogen
    return score

