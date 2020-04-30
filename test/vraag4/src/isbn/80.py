def isISBN(isbn):
    if len(isbn) != 13:
        return False
    if not isbn.isdigit():
        return False
    even = isbn[::2]
    oneven = isbn[1::2]
    someven = 0
    somoneven = 0
    for i in range(6):
        cijfer = int(even[i])
        someven += cijfer
        cijfer = int(oneven[i])
        somoneven += cijfer
    controle = (10-(someven + 3 * somoneven) %10) %10
    return controle == int(even[6])

def overzicht(codes):
    woordenboek = {"Engelstalige landen": 0,"Franstalige landen":0,"Duitstalige landen":0,"Japan":0,"Russischtalige landen":0,"China":0,"Overige landen":0,"Fouten":0}
    for item in codes:
        if isISBN(item) == False:
            woordenboek["Fouten"] += 1
        elif item[:3] == "978" or item[:3] == "979":
            if item[3] == "0" or item[3] == "1":
                woordenboek["Engelstalige landen"] += 1
            if item[3] == "2":
                woordenboek["Franstalige landen"] += 1
            if item[3] == "3":
                woordenboek["Duitstalige landen"] += 1
            if item[3] == "4":
                woordenboek["Japan"] += 1
            if item[3] == "5":
                woordenboek["Russischtalige landen"] += 1
            if item[3] == "7":
                woordenboek["China"] += 1
            if item[3] == "6" or item[3] == "8" or item[3] == "9":
                woordenboek["Overige landen"] += 1
        else:
            woordenboek["Fouten"] += 1
    for element in woordenboek:
        zin = element + ": " + str(woordenboek[element])
        print(zin)

