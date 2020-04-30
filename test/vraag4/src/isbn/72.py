def overzicht(codes):
    dictionary = {"Engelstalige landen": 0, "Franstalige landen": 0, "Duitstalige landen": 0, "Japan": 0, "Russischtalige landen": 0, "China": 0, "Overige landen": 0, "Fouten": 0}
    for code in codes:
        if not isISBN(code):
            key = "Fouten"
        else:
            if not (code[:3] == "978" or code[:3] == "979"):
                key = "Fouten"
            elif code[3] == "0" or code[3] == "1":
                key = "Engelstalige landen"
            elif code[3] == "2":
                key = "Franstalige landen"
            elif code[3] == "3":
                key = "Duitstalige landen"
            elif code[3] == "4":
                key = "Japan"
            elif code[3] == "5":
                key = "Russischtalige landen"
            elif code[3] == "7":
                key = "China"
            elif code[3] == "6" or code[3] == "8" or code[3] == "9":
                key = "Overige landen"
        dictionary[key] = int(dictionary[key]) + 1
    for item in dictionary:
        print(str(item) + ": " + str(dictionary[item]))


def isISBN(code):
    code = str(code)
    o = 0
    e = 0
    for i in range(0,12):
        if i%2 == 0:
            o += int(code[i])
        else:
            e += int(code[i])
    if int(code[12]) == ((10-(o+3*e)%10)%10):
        return True
    return False

