def overzicht(codes):
    overzicht = {'Engelstalige landen': 0, 'Franstalige landen': 0, 'Duitstalige landen': 0, 'Japan': 0, 'Russischtalige landen': 0, 'China': 0, 'Overige landen': 0, 'Fouten': 0}
    for i in codes:
        l_1 = i[:-1:2]
        l_2 = i[1::2]
        o = 0
        e = 0
        for u in l_1:
            o += int(u)
        for u in l_2:
            e += int(u)
        c = (10 - (o + 3*e)%10)%10
        if c != int(i[-1]):
            overzicht['Fouten'] += 1
        elif i[3] == "0" or i[4] == "1":
            overzicht['Engelstalige landen'] += 1
        elif i[3] == "2":
            overzicht['Franstalige landen'] += 1
        elif i[3] == "3":
            overzicht['Duitstalige landen'] += 1
        elif i[3] == "4":
            overzicht['Japan'] += 1
        elif i[3] == "5":
            overzicht['Russischtalige landen'] += 1
        elif i[3] == "7":
            overzicht['China'] += 1
        else:
            overzicht['Overige landen'] += 1
    return overzicht
        
            