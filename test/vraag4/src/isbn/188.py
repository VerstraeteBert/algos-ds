def overzicht(codes):
    engels = 0
    frans = 0
    duits = 0
    japan = 0
    russ = 0
    china = 0
    overig = 0
    fout = 0
    for i in codes:
        o = int(i[0]) + int(i[2]) + int(i[4]) + int(i[6]) + int(i[8]) + int(i[10])
        e = int(i[1]) + int(i[3]) + int(i[5]) + int(i[7]) + int(i[9]) + int(i[11])
        result = (10 - (o + 3 * e) % 10) % 10
        if result == int(i[12]) and (i[0:3]=="978" or i[0:3]=="979"):
            if int(i[3]) == 1 or int(i[3]) == 0:
                engels += 1
            elif int(i[3]) == 2:
                frans += 1
            elif int(i[3]) == 3:
                duits += 1
            elif int(i[3]) == 4:
                japan += 1
            elif int(i[3]) == 5:
                russ += 1
            elif int(i[3]) == 7:
                china += 1
            elif int(i[3]) == 6 or 10 > int(i[3]) > 7:
                overig += 1
        else:
            fout += 1
    print("Engelstalige landen: {}\nFranstalige landen: {}\nDuitstalige landen: {}\nJapan: {}\nRussischtalige landen: {}\nChina: {}\nOverige landen: {}\nFouten: {}".format(engels, frans, duits, japan, russ, china, overig, fout))