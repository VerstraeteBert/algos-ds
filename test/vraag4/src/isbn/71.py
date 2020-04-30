def isISBN_13(getal):
    if isinstance(getal, int):
        return False
    for i in range(len(getal)):
        if getal[i].isalpha():
            return False

    som1 = 0
    som2 = 0
    for i in range(1, 12, 2):
        som1 += int(getal[i - 1])
    for i in range(2, 13, 2):
        som2 += int(getal[i - 1])
    dertiende = (10 - (som1 + (3 * som2) % 10) % 10)
    if dertiende == int(getal[12]):
        return True
    elif dertiende == 10 and int(getal[12]) == 0:
        return True
    else:
        return False


def overzicht(codes):
    dict = {}
    for element in codes:
        if isISBN_13(element):
            letter = element[3]
            if letter == '0' or letter == '1':
                try:
                    teller = dict['Engelstalige landen']
                    teller += 1
                    dict['Engelstalige landen'] = teller
                except KeyError:
                    dict['Engelstalige landen'] = 1
            elif letter == '2':
                try:
                    teller = dict['Franstalige landen']
                    teller += 1
                    dict['Franstalige landen'] = teller
                except KeyError:
                    dict['Franstalige landen'] = 1
            elif letter == '3':
                try:
                    teller = dict['Duitstalige landen']
                    teller += 1
                    dict['Duitstalige landen'] = teller
                except KeyError:
                    dict['Duitstalige landen'] = 1
            elif letter == '4':
                try:
                    teller = dict['Japan']
                    teller += 1
                    dict['Japan'] = teller
                except KeyError:
                    dict['Japan'] = 1
            elif letter == '5':
                try:
                    teller = dict['Russischtalige landen']
                    teller += 1
                    dict['Russischtalige landen'] = teller
                except KeyError:
                    dict['Russischtalige landen'] = 1
            elif letter == '7':
                try:
                    teller = dict['China']
                    teller += 1
                    dict['China'] = teller
                except KeyError:
                    dict['China'] = 1
            elif letter == '6' or letter == '8' or letter == '9':
                try:
                    teller = dict['Overige landen']
                    teller += 1
                    dict['Overige landen'] = teller
                except KeyError:
                    dict['Overige landen'] = 1
        else:
            try:
                teller = dict['Fouten']
                teller += 1
                dict['Fouten'] = teller
            except KeyError:
                dict['Fouten'] = 1
    
    tuple = ('Engelstalige landen','Franstalige landen','Duitstalige landen','Japan','Russischtalige landen','China','Overige landen','Fouten')
    for element in tuple:
        print(element + ':{0:>2}'.format(dict[element]))
    