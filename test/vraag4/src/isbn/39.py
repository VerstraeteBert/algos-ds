def overzicht(codes):
    o = 0
    e = 0
    engels = 0
    frans = 0
    duits = 0
    japan = 0
    rus = 0
    china = 0
    overig = 0
    fout = 0
    for code in codes:
        for i in range(13):
            getal = int(code[i])
            if getal % 2 == 0:
                e += getal
            else:
                o += getal
        x13 = (10 - (o + 3*e) % 10) % 10
        if x13 == int(code[12]) and int(code[0:2]) == 978 or int(code[0:2]) == 979:
            vierde = code[3]
            if 0 <= vierde <= 1:
                engels += 1
            elif vierde == 2:
                frans += 1
            elif vierde == 3:
                duits += 1
            elif vierde == 4:
                japan += 1
            elif vierde == 5:
                rus += 1
            elif vierde == 7:
                china += 1
            else:
                overig += 1
        else:
            fout += 1
    print("Engelstalige landen:", engels)
    print("Franstalige landen:", frans)
    print("Duitstalige landen:", duits)
    print("Japan:", japan)
    print("Russischtalige landen:", rus)
    print("China:", china)
    print("Overige landen:", overig)
    print("Fouten:", fout)

            