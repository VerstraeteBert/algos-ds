def overzicht(codes):

    groepen = {}
    for i in range(11):
        groepen[i] = 0
    a = 0
    c = ""
    el = 0
    while a < len(codes):
        c = codes[a]
        t = geldig(c)
        if t == False:
            groepen[10] += 1
        else:
            if controleerCD(c) == False:
                groepen[10] += 1
            else:
                if int(c[3:4]) == 0:
                    groepen[0] += 1
                if int(c[3:4]) == 1:
                    groepen[1] += 1
                if int(c[3:4]) == 2:
                    groepen[2] += 1
                if int(c[3:4]) == 3:
                    groepen[3] += 1
                if int(c[3:4]) == 4:
                    groepen[4] += 1
                if int(c[3:4]) == 5:
                    groepen[5] += 1
                if int(c[3:4]) == 7:
                    groepen[7] += 1
                if int(c[3:4]) == 6:
                    groepen[6] += 1
                if int(c[3:4]) == 8:
                    groepen[8] += 1
                if int(c[3:4]) == 9:
                    groepen[9] += 1


        a += 1



    print("Engelstalige landen:" , (groepen[0] + groepen[1]))
    print("Franstalige landen:", (groepen[2]))
    print("Duitstalige landen:", (groepen[3]))
    print("Japan:", (groepen[4]))
    print("Russischtalige landen:", (groepen[5]))
    print("China:", (groepen[7]))
    print("Overige landen:", (groepen[6] + groepen[8]) + groepen[9])
    print("Fouten:", groepen[10])


def geldig(c):

    if int(c[:3]) == 978 or int(c[:3]) == 979:
        return True
    else:
        return False



def controleerCD(c):
    o = 0
    e = 0
    o = int(c[0]) + int(c[2]) + int(c[4]) + int(c[6]) + int(c[8]) + int(c[10])
    e = int(c[1]) + int(c[3]) + int(c[5]) + int(c[7]) + int(c[9]) + int(c[11])
    p = 10 - (int(o)+(3*(int(e))))
    x13 = p % 10
    j = int(c[12:13])

    if x13 == j:

        return True
    else:

        return False