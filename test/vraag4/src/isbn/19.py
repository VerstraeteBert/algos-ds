def overzicht (codes):
    dictionary = {'Engelstalige landen:':0, 'Franstalige landen:':0, 'Duitstalige landen:':0, 'Japan:':0,'Russischtalige landen:':0, 'China:':0, 'Overige landen:':0, 'Fouten:':0}
    lijst = codes
    for el in lijst:
        o = 0
        e = 0
        x13 = el[12]
        for i in range (0,12,2):
            o += int(el[i])
        for i in range (1,12,2):
            e += int(el[i])
        correction = (10-(o+3*e)%10)%10
        if correction != int(x13):
            dictionary['Fouten:'] = dictionary["Fouten:"] + 1
        else:
            if el[0] == '9' and el[1]=='7' and (el[2]=='8' or el[2]=='9'):
                if el[3] == '0' or el[3]=='1':
                    dictionary['Engelstalige landen:'] =  dictionary['Engelstalige landen:'] +1
                if el[3] == '2':
                    dictionary['Franstalige landen:'] = dictionary['Franstalige landen:'] + 1
                if el[3]== '3':
                    dictionary['Duitstalige landen:'] = dictionary['Duitstalige landen:'] + 1
                if el[3]== '4':
                    dictionary['Japan:'] = dictionary['Japan:'] + 1
                if el[3]== '5':
                    dictionary['Russischtalige landen:'] = dictionary['Russischtalige landen:'] + 1
                if el[3]== '7':
                    dictionary['China:'] = dictionary['China:'] + 1
                if el[3] == '6' or el[3] == '8' or el[3] == '9':
                    dictionary['Overige landen:'] = dictionary['Overige landen:'] + 1
            else:
                dictionary['Fouten:'] = dictionary["Fouten:"] + 1

    for naam, aantal in dictionary.items():
        print (naam, aantal)



