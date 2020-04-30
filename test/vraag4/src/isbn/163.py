landen = {'1': 'Engelstalige landen',
         '2': 'Franstalige landen',
         '3': 'Duitstalige landen',
         '4': 'Japan',
         '5': 'Russischtalige landen',
         '7': 'China',
         '6': 'Overige landen'}






def isISBN_13(isbn):
    if not type(isbn) is str:
        return False
    if len(isbn) != 13:
        return False
    if not isbn.isdigit():
        return False
    even = isbn[::2]
    oneven = isbn[1::2]
    som_even = 0
    som_oneven = 0
    for i in range(6):
        cijfer = int(even[i])
        som_even += cijfer
        cijfer = int(oneven[i])
        som_oneven += cijfer
    controle = (10 - (som_even + 3 * som_oneven) %10) %10

    return controle == int(isbn[12])

def overzicht(codes):
    aantal = {'Engelstalige landen': 00,
              'Franstalige landen': 00,
              'Duitstalige landen': 00,
              'Japan': 00,
              'Russischtalige landen': 00,
              'China': 00,
              'Overige landen': 00,
              'Fouten': 00}
    for i in codes:
        if i[:3] in ('978', '979'):
            if isISBN_13(i) == True:
                getal = i[3]
                if getal == '8' or getal == '9':
                    getal = '6'
                elif getal == '0':
                    getal = '1'
                aantal[landen[getal]] += 1
            else:
                aantal['Fouten'] += 1
        else:
            aantal['Fouten'] += 1
    for land in aantal:
        print("{}: {}".format(land, aantal[land]))