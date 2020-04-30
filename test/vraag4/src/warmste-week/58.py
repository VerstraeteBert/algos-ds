def gift_inschrijven(klasbed, dic):
    klas = klasbed[0]
    #print(klas)  # test
    bed = klasbed[1]
    #print(bed)  # test
    if klas in dic:
        bed += dic[klas]
        dic[klas] = bed
    else:
        dic[klas] = bed
    return dic
