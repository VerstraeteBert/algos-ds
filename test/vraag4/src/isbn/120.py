def isbn_controleren(code):
    for karakter in code:
        if karakter not in "0987654321":
            return False
            
    x_1 = 0
    x_2 = 0
    
    for karakter in range(0, 12, 2):
        x_1 += int(code[karakter])
    for karakter in range(1, 12, 2):
        x_2 += int(code[karakter])
    
    controlegetal = (10 - (x_1 + 3*x_2)%10)%10
    return str(controlegetal) == code[12]


def overzicht(codes):
    Landenlijst = {"Engelstalige landen": 0, "Franstalige landen": 0, "Duitstalige landen": 0, "Japan": 0, "Russischtalige landen": 0, "China": 0, "Overige landen": 0, "Fouten": 0} 
    Nummerslijst = {"0": "Engelstalige landen", "1": "Engelstalige landen", "2": "Franstalige landen", "3": "Duitstalige landen", "4": "Japan", "5": "Russischtalige landen", "7": "China", "6": "Overige landen", "8": "Overige landen", "9": "Overige landen"}
    for isbn in codes:
        if isbn_controleren(isbn) == False:
            Landenlijst["Fouten"] += 1
        else:
            if "978" == isbn[0:3:] or isbn[0:3:] == "979":
                land = Nummerslijst[isbn[3]]
                Landenlijst[land] += 1
            else:
                Landenlijst["Fouten"] += 1
    for x,y in Landenlijst.items():
        print("{}: {}".format(x, y))