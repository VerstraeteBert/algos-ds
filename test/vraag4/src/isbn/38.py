def isISBN_13(isbn):           # 13 cijferige isbn
    if isbn != str(isbn):               # nagaan of de isbn code inderdaad een string is bij het ingeven
        return False
    o_index, e_index = 0, 0                             # som gelijkstellen aan nul
    for index in range(0,12):            # alle karakters overlopen
        if isbn[index].isalpha():  # nagaan of het te overlopen karakter effectief een getal is
            return False
        elif (index+1) % 2:           # oneven componenten van de code
            o_index += int(isbn[index])
            # print(o_index, e_index)
        else:
            e_index += int(isbn[index])
            # print(o_index, e_index)
    controle = ((10 - (o_index + 3 * e_index) % 10) % 10)
    # print(o_index, e_index)
    if isbn[12] == "X":
        return False
    else:
        return controle == int(isbn[12])      # returns True or False

def overzicht(codes):
    ean = {"Engelstalige landen:": [0, "0", "1"], "Franstalige landen:": [0, "2"], "Duitstalige landen:": [0, "3"], "Japan:": [0, "4"],
           "Russischtalige landen:": [0, "5"], "China:": [0, "7"], "Overige landen:": [0, "6", "8", "9"], "Fouten:": [0]}
    for code in codes:
        if isISBN_13(code) and (code[0:3]== "978" or code[0:3] == "979"):
            for key in ean:
                if code[3] in ean[key]:
                    ean[key][0] += 1
        else:
            ean["Fouten:"][0] += 1
    for sleutel in ean:
        print("{} {}".format(sleutel,ean[sleutel][0]))