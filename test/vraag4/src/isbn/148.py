
def overzicht(codes):
    overzicht_aantal = {
            "Engelstalige landen": 0,
            "Franstalige landen": 0,
            "Duitstalige landen": 0,
            "Japan": 0,
            "Russischtalige landen": 0,
            "China": 0,
            "Overige landen": 0,
            "Fouten": 0
            }
    overzicht_landen = {
            0: "Engelstalige landen",
            1: "Engelstalige landen",
            2: "Franstalige landen",
            3: "Duitstalige landen",
            4: "Japan",
            5: "Russischtalige landen",
            6: "Overige landen",
            7: "China",
            8: "Overige landen",
            9: "Overige landen"
            }
    
    for code in codes:
        o = 0
        e = 0
        i = 0
        while i < len(code)-1:
            o += int(code[i]) * (i%2 == 0)
            e += int(code[i]) * (i%2 == 1)
            i += 1
        x13 = (10 - (o + 3*e)%10)%10
        if x13 == int(code[12]) and (code[:3] == "978" or code[:3] == "979") :
            land = overzicht_landen[int(code[3])]
            overzicht_aantal[land] += 1
        else:
            overzicht_aantal["Fouten"] += 1
    
    for land in overzicht_aantal:
        print("{}: {}".format(land, overzicht_aantal[land]))
