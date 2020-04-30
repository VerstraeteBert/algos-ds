def overzicht(codes):
    fouten = 0
    eng = 0
    fr = 0
    dui = 0
    jap = 0
    rus = 0
    chin = 0
    rest = 0
    for code in codes:
        if 977 < int(code[0:2]) < 980:
            if code[3:3] == 0 or code[3:3] == 1:
                eng += 1
            elif code[3:3] == 2:
                fr += 1
            elif code[3:3] == 3:
                dui += 1
            elif code[3:3] == 4:
                jap += 1
            elif code[3:3] == 5:
                rus += 1
            elif code[3:3] == 7:
                chin += 1
            else:
                rest += 1
        else:
            fouten += 1
    print("Engelstalige landen:", {}, '\n', "Franstalige landen:", {}, '\n', "Duitstalige landen:", {}, '\n', "Japan:", {}, '\n', "Russische landen:", {}, '\n', 'China:', {}, '\n', "Overige landen:", {}, '\n', "Fouten:", {}, .format(eng, fr, dui, jap, rus, rest, fouten))