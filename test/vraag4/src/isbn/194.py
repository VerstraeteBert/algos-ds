def isISBN_13(code):
    if len(code) != 13:
        return False
        
    if code[:3] != "978" and code [:3] != "979":
        return False
    even = code[::2]
    oneven = code[1::2]
    someven = 0
    somoneven = 0
    for i in range(6):
        cijfer = int(even[i])
        someven += cijfer
        cijfer = int(oneven[i])
        somoneven += cijfer
    controle = (10-(someven + 3 * somoneven) %10)%10

    return controle == int(even[6])

def overzicht(codes):
    verzameling = {
        'Engelstalige landen': 0,
        'Franstalige landen': 0,
        'Duitstalige landen': 0,
        'Japan': 0,
        'Russischtalige landen': 0,
        'China': 0,
        'Overige landen': 0,
        'Fouten': 0 
    }
    for code in codes:
        if code[:3] not in ('978', '979') or not isISBN_13(code):
            verzameling['Fouten'] += 1
        elif code[3] in ('0', '1'):
            verzameling['Engelstalige landen'] += 1
        elif code[3] in ('2'):
            verzameling['Franstalige landen'] += 1
        elif code[3] in ('3'):
            verzameling['Duitstalige landen'] += 1
        elif code[3] in ('4'):
            verzameling['Japan'] += 1
        elif code[3] in ('5'):
            verzameling['Russischtalige landen'] += 1
        elif code[3] in ('7'):
            verzameling['China'] += 1
        elif code[3] in ('6', '8', '9'):
            verzameling['Overige landen'] += 1

    for item in verzameling:
        print(item, ': ', verzameling[item], sep='')