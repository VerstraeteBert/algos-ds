def overzicht(codes):
    fouten = 0
    engels = 0
    frans = 0
    duits = 0
    japan = 0
    russisch = 0
    chinees = 0
    overig = 0
    for code in codes:
        o = int(code[0]) + int(code[2]) + int(code[4]) + int(code[6]) + int(code[8]) + int(code[10])
        e = int(code[1]) + int(code[3]) + int(code[5]) + int(code[7]) + int(code[9]) + int(code[11])
        dertien = (10 - (o+3*e) % 10) % 10
        if int(code[0]) == 9 and int(code[1]) == 7 and int(code[2]) in [8, 9] and int(code[12]) == dertien:
            if int(code[3]) in [0, 1]:
                engels += 1
            if int(code[3]) == 2:
                frans += 1
            if int(code[3]) == 3:
                duits += 1
            if int(code[3]) == 4:
                japan += 1
            if int(code[3]) == 5:
                russisch += 1
            if int(code[3]) == 7:
                chinees += 1
            if int(code[3]) in [6, 8, 9]:
                overig += 1
        else:
            fouten += 1
    print("Engelstalige landen:", engels)
    print("Franstalige landen:", frans)
    print("Duitstalige landen:", duits)
    print("Japan:", japan)
    print("Russischtalige landen:", russisch)
    print("China:", chinees)
    print("Overige landen:", overig)
    print("Fouten:", fouten)
