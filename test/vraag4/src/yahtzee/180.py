def histogram(stenen):
    histo_dict = {}
    for steen in stenen:
        if steen in histo_dict:
            histo_dict[steen] += 1  # if steen al in histo_dict staat tel 1 bij value
        else:
            histo_dict[steen] = 1   # key steen nog niet in  
    return histo_dict       
    
def max_gelijk(stenen):
    histo_dict = histogram(stenen)
    max_val = max(histo_dict.values())
    return max_val
    
def is_FullHouse(stenen):
    fullhouse = False
    histo_dict = histogram(stenen)
    fullhouse = bool(max(histo_dict.values()) == 3 and len(histo_dict) == 2)
    #if max(histo_dict.values()) == 3 and len(histo_dict) == 2:  # maximum value is 3 en lengte van dict is 2 dan full house
    #    fullhouse = True
    #else:
    #    fullhouse = False
    return fullhouse    
        
        
def som(stenen):
    i = 0
    som = 0
    for i in stenen:  # ga elke waarde af in list result
        som += i   #tel elke waarde op
    return som
    
def is_Yathzee(stenen):
    first_number = 0
    count = 0
    yathzee = False
    first_number = stenen[0]        # get first number in stenen
    length = len(stenen)            # count entries in list stenen
    
    for i in stenen:
        if i == first_number:
            count += 1
    if count == length:
        yathzee = True
    return yathzee
    
def is_grote_straat(stenen):
    grote_straat = False
    first = 0
    second = 0
    count = 0
    length = 0
    i = 0
    length = len(stenen)            # lengte list stenen
    stenen.sort() 
    for i in range(0, len(stenen) - 1, 1):
        first = stenen[i]           # haal eerste element uit list stenen
        second = stenen[i + 1]          # haal tweede element uit list stenen
        if second == first + 1:      # check of het tweede element 1 hoger is dan eerste element
            count += 1               # indien True dan count plus 1
    if count == length - 1:         # als count = lengte list stenen - 1 dan grote straat
        grote_straat = True
    return grote_straat
    
def is_kleine_straat(stenen):
    kleine_straat = False
    first = 0
    second = 0
    count = 0
    length = 0
    i = 0
    length = len(stenen)            # lengte list stenen
    stenen.sort() 
    for i in range(0, len(stenen) - 1, 1):
        first = stenen[i]           # haal eerste element uit list stenen
        second = stenen[i + 1]          # haal tweede element uit list stenen
        if second == first + 1 and count == 0:      # check of het tweede element 1 hoger is dan eerste element
            count += 2               # indien True dan count plus 1
        elif second == first + 1 and count != 0:
            count += 1
        elif second > first + 1 and count != 4:
            count = 0
    if count == length - 1:         # als count = lengte list stenen - 1 dan grote straat
        kleine_straat = True
    return kleine_straat
    
def grootste_score(stenen):
    totaal = 0
    if is_Yathzee(stenen):          # 5 dezelfde stenen
        totaal += 50
    elif is_grote_straat(stenen):   # 5 oplopende stenen 
        totaal += 40
    elif is_kleine_straat(stenen):  # 4 oplopende stenen
        totaal += 30
    elif is_FullHouse(stenen):      # 3 dezelfde en 1 paar
        if som(stenen) > 25:
            totaal = som(stenen)
        else: 
            totaal += 25
    elif max_gelijk(stenen) == 4:    # 4 dezelfde 
        totaal += som(stenen)
    elif max_gelijk(stenen) == 3:    # 3 dezelfde
        totaal += som(stenen)
    else:                                # willekeurig
        totaal += som(stenen)
    return totaal
    