landen_codes = {
    "Engelstalige landen": [0, 1], 
    "Franstalige landen": [2], 
    "Duitstalige landen": [3], 
    "Japan": [4], 
    "Russischtalige landen": [5], 
    "China": [7], 
    "Overige landen": [6, 8, 9]
}

def overzicht(codes):
    overzicht = {
       "Engelstalige landen": 0,
       "Franstalige landen": 0,
       "Duitstalige landen": 0,
       "Japan": 0,
       "Russischtalige landen": 0,
       "China": 0,
       "Overige landen": 0,
       "Fouten": 0
    }
    
    for code in codes:
        o = 0
        for i in range(0, 12, 2):
            o += int(code[i])
            
        e = 0
        for i in range(1,13, 2):
            e += int(code[i])
        
        controle_cijfer = ((10 - (o + 3 * e) % 10) % 10)
        
        if ((code[:3] == "978" or code[:3] == "979") and int(code[12]) == controle_cijfer):
            for land, cijfers in landen_codes.items():
                if int(code[3]) in cijfers:
                    overzicht[land] += 1
        else:
            overzicht["Fouten"] += 1
    
    for land, aantal in overzicht.items():
        print(land + ": " + str(aantal))