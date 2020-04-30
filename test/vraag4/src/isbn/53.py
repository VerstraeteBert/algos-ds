def isISBN_13(nummer):
    if not type(nummer) is str:
        return False
    o = 0
    e = 0
    o_getal =nummer[:12:2]
    e_getal = nummer[1:12:2]

    for i in o_getal:
        if i == 'X':
            o+= 10
        elif i.isdigit():
            i = int(i)
            o += i
        else:
            return False
    for i in e_getal:
        if i == 'X':
            e += 10
        elif i.isdigit():
            i = int(i)
            e += i
        else:
            return False

    controle = (10 - ((o + 3 * e) % 10)) % 10
    if nummer[12] != 'X':
        if int(nummer[12]) == controle:
            return True
    else:
        if 10 == controle:
            return True
    return False


def overzicht(codes):
    #array_isbn = codes.split(', ')
    dictionary = {'Engelstalige landen': 0, 'Franstalige landen': 0, 'Duitstalige landen': 0, 'Japan': 0, 'Russischtalige landen': 0, 'China': 0, 'Overige landen': 0, 'Fouten': 0}
    for isbn in codes:
        if isbn[0]== '9' and isbn[1]=='7' and (isbn[2]== '8' or isbn[2]=='9') and isISBN_13(isbn):
            if isbn[3]== '0' or isbn[3] == '1':
                dictionary['Engelstalige landen'] += 1
            elif isbn[3]== '2':
                dictionary['Franstalige landen'] += 1
            elif isbn[3]== '3':
                dictionary['Duitstalige landen'] += 1
            elif isbn[3]== '4':
                dictionary['Japan'] += 1
            elif isbn[3]== '5':
                dictionary['Russischtalige landen'] += 1
            elif isbn[3]== '7':
                dictionary['China'] += 1
            elif isbn[3]== '6' or isbn[3] == '8'or isbn[3] == '9':
                dictionary['Overige landen'] += 1
        else:
            dictionary['Fouten'] += 1

    for land, aantal in dictionary.items():
        print(land + ':', aantal)


