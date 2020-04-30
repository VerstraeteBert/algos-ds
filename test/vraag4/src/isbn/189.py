def overzicht(codes):
    dic = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
    for x in codes:
        land = int(x[3])
        if land == 0:
            land = 1
        elif land in (8, 9):
            land = 6
        geldig = True
        if int(x[0:3]) in (978, 979):
            o = int(x[0]) + int(x[2]) + int(x[4]) + int(x[6]) + int(x[8]) + int(x[10])
            e = int(x[1]) + int(x[3]) + int(x[5]) + int(x[7]) + int(x[9]) + int(x[11])
            k = (10 - (o + 3 * e) % 10) % 10
            if int(x[12]) != k:
                geldig = False
        else:
            geldig = False
        if geldig:
            dic[land] += 1
        else:
            dic[0] += 1
    print("Engelstalige landen: " + str(dic[1]))
    print("Franstalige landen: " + str(dic[2]))
    print("Duitstalige landen: " + str(dic[3]))
    print("Japan: " + str(dic[4]))
    print("Russischtalige landen: " + str(dic[5]))
    print("China: " + str(dic[7]))
    print("Overige landen: " + str(dic[6]))
    print("Fouten: " + str(dic[0]))