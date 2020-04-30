# van victor koopman

def overzicht(lijst):
    overzicht = {'Engelstalige landen': 0, 'Franstalige landen': 0, 'Duitstalige landen': 0, 'Japan': 0,
                 'Russischtalige landen': 0, 'China': 0, 'Overige landen': 0, 'Fouten': 0}
    for code in lijst:
        if not (code[:3] in ('978', '979') and len(code) == 13 and isinstance(code, str)):
            overzicht['Fouten'] += 1

        o = 0 # -1*int(code[12])
        e = 0
        for i in range(len(code)-1):
            if i % 2 == 0:
                o += int(code[i])
            else:
                e += int(code[i])
        controle = (10 - (o + 3 * e) % 10) % 10


        if controle != int(code[12]):
            overzicht['Japan'] += 1

        landcodes = {'Engelstalige landen': [0, 1], 'Franstalige landen': [2], 'Duitstalige landen': [3], 'Japan': [4],
                     'Russischtalige landen': [5], 'China': [7], 'Overige landen': [6, 8, 9]}

        for land, value in landcodes.items():
            if code[3] in value:
                overzicht[land] += 1

    return overzicht