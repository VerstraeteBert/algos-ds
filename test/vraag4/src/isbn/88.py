def overzicht(lijst):
    overzicht = {'Engelstalige landen': 0, 'Franstalige landen': 0, 'Duitstalige landen': 0, 'Japan': 0,
                 'Russischtalige landen': 0, 'China': 0, 'Overige landen': 0, 'Fouten': 0}
    for code in lijst:
        if not (code[:3] in ('978', '979') and len(code) == 13 and isinstance(code, str)):
            overzicht['Fouten'] += 1
            continue

        o = 0
        e = 0
        for i in range(len(code) - 1):
            if i % 2 == 0:
                o += int(code[i])
            else:
                e += int(code[i])
        controle = (10 - (o + 3 * e) % 10) % 10

        if controle != int(code[12]):
            overzicht['Fouten'] += 1
            continue

        landcodes = {0: 'Engelstalige landen', 1: 'Engelstalige landen', 2: 'Franstalige landen',
                     3: 'Duitstalige landen', 4: 'Japan', 5: 'Russischtalige landen', 6: 'Overige landen', 7: 'China',
                     8: 'Overige landen', 9: 'Overige landen'}

        for getal, land in landcodes.items():
            if int(code[3]) == getal:
                overzicht[land] += 1

    for land, getal in overzicht.items():
        print('{}: {}'.format(land, getal))