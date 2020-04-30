def histogram(stenen):
    boek = {}
    for oog in stenen:
        aantal = stenen.count(oog)
        boek[oog] = aantal
    return boek
def max_gelijk(stenen):
    maximum = 0
    for oog in stenen:
        aantal = stenen.count(oog)
        if aantal > maximum:
            maximum = aantal
    return maximum
def is_FullHouse(stenen):
    correct = 0
    for oog in stenen:
        aantal = stenen.count(oog)
        if aantal == 2 or aantal == 3:
            correct += 1
    return correct == 5

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
def grootste_score(stenen):
    score = 0
    if is_Yathzee(stenen):
        score = 50
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
            