def overzicht(lijst_code):
    fouten = 0
    engels = 0
    frans = 0
    duits = 0
    japans = 0
    rus = 0
    china = 0
    overig = 0
    for string in lijst_code:
        x1 = int(string[0])
        x2 = int(string[1])
        x3 = int(string[2])
        x4 = int(string[3])
        x5 = int(string[4])
        x6 = int(string[5])
        x7 = int(string[6])
        x8 = int(string[7])
        x9 = int(string[8])
        x10 = int(string[9])
        x11 = int(string[10])
        x12 = int(string[11])
        x13 = int(string[12])
        O = x1 + x3 + x5 + x7 + x9 + x11
        E = x2 + x4 + x6 + x8 + x10 + x12

        if string[0:3] == '978' or string[0:3] == '979':
            if x13 == ((10 - (O +3*E)) % 10) % 10:
                if x4 == 0 or x4 == 1:
                    engels +=1
                elif x4 == 2:
                    frans +=1
                elif x4 == 3:
                    duits += 1
                elif x4 == 4:
                    japans += 1
                elif x4 == 5:
                    rus += 1
                elif x4 == 7:
                    china += 1
                else:
                    overig += 1
            else:
                fouten += 1
        else:
            fouten += 1
    print(f'Engelstalige landen: {engels}')
    print(f'Franstalige landen: {frans}')
    print(f'Duitstalige landen: {duits}')
    print(f'Japan: {japans}')
    print(f'Russischtalige landen: {rus}')
    print(f'China: {china}')
    print(f'Overige landen: {overig}')
    print(f'Fouten: {fouten}')

