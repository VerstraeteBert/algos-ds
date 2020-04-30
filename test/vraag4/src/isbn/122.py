dict = {
    "Engelstalige landen": 0,
    "Franstalige landen": 0,
    "Duitstalige landen": 0,
    "Japan": 0,
    "Russischtalige landen": 0,
    "China": 0,
    "Overige landen": 0,
    "Fouten": 0
}
def controle(code):
    controle = code[:3]
    if controle == "978" or controle == "979":
        if len(code) != 13:
            return False
        
        try:
            int(code)
        except:
            return False
        
        o = 0
        e = 0
        for i in range(0, len(code)-1, 2):
            o += int(code[i])
        for i in range(1, len(code)-1, 2):
            e += int(code[i])
        
        controlecijfer = o + 3*e
        controlecijfer = controlecijfer % 10
        controlecijfer = (10 - controlecijfer) % 10
        if int(code[12]) == controlecijfer:
            return True
        else:
            return False
    

def overzicht(codes):
    for code in codes:
        if controle(code):
            land = code[3:4]
            if land == "0" or land == "1":
                dict["Engelstalige landen"] += 1
            elif land == "2":
                dict["Franstalige landen"] += 1
            elif land == "3":
                dict["Duitstalige landen"] += 1
            elif land == "4":
                dict["Japan"] += 1
            elif land == "5":
                dict["Russischtalige landen"] += 1
            elif land == "6":
                dict["China"] += 1
            elif land == "7" or land == "8" or land == "9":
                dict["Overige landen"] += 1
                
        else:
            dict["Fouten"] += 1
    
    for taal, aantal in dict.items():
        print("{}: {}".format(taal, aantal))