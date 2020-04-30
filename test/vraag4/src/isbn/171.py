def overzicht(codes):
    dict = {"Engelstalige landen" : 0, "Franstalige landen" : 0,"Duitstalige landen" : 0, "Japan" : 0, "Russischtalige landen" : 0,"China" : 0,"Overige landen" : 0, "Fouten" : 0}

    for i in range(0, len(codes)):
        if isISBN_13(codes[i]):
            if codes[i][0:3] == "978" or codes[i][0:3] == "979":
                if int(codes[i][3]) == 0 or int(codes[i][3]) == 1:
                    dict["Engelstalige landen"] += 1
                elif int(codes[i][3]) == 2:
                    dict["Franstalige landen"] += 1
                elif int(codes[i][3]) == 3:
                    dict["Duitstalige landen"] += 1
                elif int(codes[i][3]) == 4:
                    dict["Japan"] += 1
                elif int(codes[i][3]) == 5:
                    dict["Russischtalige landen"] += 1
                elif int(codes[i][3]) == 7:
                    dict["China"] += 1
                else:
                    dict["Overige landen"] += 1
            else:
                dict["Fouten"] += 1
        else:
            dict["Fouten"] += 1
            #for j in range(1, 10):
            #   if int(codes[i][3]) == j:
            #        dict.value()[j - 1] += 1
            #    if int(codes[i][3]) == j:
            #        dict.value()[j-1] += 1

    print("Engelstalige landen:", dict["Engelstalige landen"])
    print("Franstalige landen:", dict["Franstalige landen"])
    print("Duitstalige landen:", dict["Duitstalige landen"])
    print("Japan:", dict["Japan"])
    print("Russischtalige landen:", dict["Russischtalige landen"])
    print("China:", dict["China"])
    print("Overige landen:", dict["Overige landen"])
    print("Fouten:", dict["Fouten"])
def isISBN_13(isbn):

    if type(isbn) is str and len(isbn) == 13:
        oo = 0
        ee = 0
        i = 0
        j = 1
        while i < 12:
            sbn = isbn[i]
            if sbn.isdigit():
                oo += int(sbn)
            i += 2
        while j < 12:
            sbn = isbn[j]
            if sbn.isdigit():
                ee += int(sbn)
            j += 2
        a = isbn[12]
        if a.isdigit():
            if (oo + (3*ee) + int(a)) % 10 == 0:
                return True
            else:
                return False
        else: return False
    else: return False
