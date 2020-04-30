def overzicht(lijst):
    catego = {}
    catego["Engelstalige landen"] = []      # dictionary keys aanmaken
    catego["Franstalige landen"] = []
    catego["Duitstalige landen"] = []
    catego["Japan"] = []
    catego["Russischtalige landen"] = []
    catego["China"] = []
    catego["Overige landen"] = []
    catego["Fouten"] = []
    for code in lijst:      # geen isbn
        if code[:3] != "978" and code[:3] != "979":
            catego["Fouten"].append(code)
            lijst.remove(code)
    for code in lijst:
        ooo = code[:12:2]
        oo = list(ooo)
        o = sum([int(i) for i in oo])
        eee = code[1::2]
        ee = list(eee)
        e = sum([int(i) for i in ee])
        if code[12] in str((10-(o+(3*e)) % 10) % 10):
            continue
        else:
            catego["Fouten"].append(code)
            lijst.remove(code)          # nu zijn alle foute isbn's eruit
    for code in lijst:  # sorteren
        if code[3] in "01":
            catego["Engelstalige landen"].append(code)
        if code[3] in "2":
            catego["Franstalige landen"].append(code)
        if code[3] in "3":
            catego["Duitstalige landen"].append(code)
        if code[3] in "4":
            catego["Japan"].append(code)
        if code[3] in "5":
            catego["Russischtalige landen"].append(code)
        if code[3] in "7":
            catego["China"].append(code)
        if code[3] in "689":
            catego["Overige landen"].append(code)
    for land in catego:
        print("{}: {}".format(land, len(catego[land])))     # optellen