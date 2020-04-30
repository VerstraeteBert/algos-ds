def overzicht(codes):
    eng = 0
    fran = 0
    duits = 0
    jap = 0
    russ = 0
    chin = 0
    over = 0
    fout = 0
    for code in codes:
        o = 0
        e = 0
        voorwaarde_1 = False
        voorwaarde_2 = False
        for i in range(0,12,2):
            o += int(code[i:i+1])
        for k in range(1,12,2):
            e += int(code[k:k+1])
        x13 = (10-(o+3*e)%10)%10
        if int(code[12:]) == x13:
            voorwaarde_1 = True
        if code[:3] == "978" or code[0:3] == "979":
            voorwaarde_2 = True
        if voorwaarde_1 == True and voorwaarde_2 == True:
            if code[3:4] == "0" or code[3:4] == "1":
                eng += 1
            if code[3:4] == "2":
                fran += 1
            if code[3:4] == "3":
                duits += 1
            if code[3:4] == "4":
                jap += 1
            if code[3:4] == "5":
                russ += 1
            if code[3:4] == "7":
                chin += 1
            if code[3:4] == "6" or code[3:4] == "8" or code[3:4] == "9":
                over += 1
    totaal = eng + fran + duits + jap + russ + chin + over
    fouten = len(codes) - totaal
    print("Engelstalige landen: {}".format(eng))
    print("Franstalige landen: {}".format(fran))
    print("Duitstalige landen: {}".format(duits))
    print("Japan: {}".format(jap))
    print("Russischtalige landen: {}".format(russ))
    print("China: {}".format(chin))
    print("Overige landen: {}".format(over))
    print("Fouten: {}".format(fouten))