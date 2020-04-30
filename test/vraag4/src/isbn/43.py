def overzicht(lijst):
    engels = 0
    frans = 0
    duits = 0
    japan = 0
    rus = 0
    china = 0
    overig = 0
    fouten = 0
    for isbn in lijst:
        isbn = str(isbn)
        if int(isbn[:3])== 978 or int(isbn[:3])== 979:
            o = 0
            for i in range(0,11,2):
                o += int(isbn[i])
            e = 0
            for i in range(1,12,2):
                e += int(isbn[i])
            x13 = (10-(o+3*e)%10)%10
            if x13 == int(isbn[12]):
                if int(isbn[3])== 0 or int(isbn[3])== 1:
                    engels +=1
                elif int(isbn[3])== 2:
                    frans +=1
                elif int(isbn[3]) == 3:
                    duits +=1
                elif int(isbn[3]) == 4:
                    japan +=1
                elif int(isbn[3]) == 5:
                    rus +=1
                elif int(isbn[3]) == 7:
                    china += 1
                else:
                    overig +=1
            else:
                fouten +=1
        else:
            fouten +=1
    print("Engelstalige landen:", engels)
    print("Franstalige landen:", frans)
    print("Duitstalige landen:", duits)
    print("Japan:", japan)
    print("Russischtalige landen:", rus)
    print("China:", china)
    print("Overige landen:", overig)
    print("Fouten:", fouten)