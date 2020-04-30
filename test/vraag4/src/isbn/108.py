def overzicht(c):
    d = {"Engelstalige landen:" : 0, "Franstalige landen:" : 0, "Duitstalige landen:" : 0,
        "Japan:" : 0, "Russischtalige landen:" : 0, "China:" : 0, "Overige landen:" : 0, "Fouten:" : 0}
    for l in c:
        o = 0
        e = 0
        for i in range(0,12,2):
            o += int(l[i])
            e += int(l[i+1])
        if int(l[12]) == ((10 -(o+3*e)%10)%10):
            if l[:3] == "978" or l[:3] == "979":
                if l[3] == "0" or l[3] == "1":
                    d["Engelstalige landen:"] += 1
                elif l[3] == "2":
                    d["Franstalige landen:"] += 1
                elif l[3] == "3":
                    d["Duitstalige landen:"] += 1
                elif l[3] == "4":
                    d["Japan:"] += 1
                elif l[3] == "5":
                    d["Russischtalige landen:"] += 1
                elif l[3] == "7":
                    d["China:"] += 1
                else:
                    d["Overige landen:"] += 1
            else:
                d["Fouten:"] += 1
        else:
            d["Fouten:"] += 1
    for el in d:
        print(el, d[el])