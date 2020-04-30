def ISBN(code):
    o, e = 0, 0
    for pos in range(len(code)-1):
        o += int(code[pos])*((pos+1)%2)
        e += int(code[pos])*(pos%2)
    return int(code[-1]) == ((10-(o+3*e))%10)%10

def overzicht(str_list):
    start = ['978', '979']
    boek = {'Engelstalige landen':0,'Franstalige landen':0,'Duitstalige landen':0,'Japan':0,'Russischtalige landen':0, 'China':0, 'Overige landen':0, 'Fouten':0}
    for code in str_list:
        if not ISBN(code) or code[:3] not in start:
            boek['Fouten'] += 1
        elif code[3] == '0' or  code[3] == '1':
            boek['Engelstalige landen'] += 1
        elif code[3] == '2':
            boek['Franstalige landen'] += 1
        elif code[3] == '3':
            boek['Duitstalige landen'] += 1
        elif code[3] == '4':
            boek['Japan'] += 1
        elif code[3] == '5':
            boek['Russischtalige landen'] += 1
        elif code[3] == '7':
            boek['China'] += 1
        else:
            boek['Overige landen'] += 1
    for key in boek.keys():
        lijn = '{}: {}'.format(key,boek[key])
        print(lijn)