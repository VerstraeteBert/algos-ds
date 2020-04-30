mapping = ['Engelstalige landen', 'Engelstalige landen', 'Franstalige landen', 'Duitstalige landen',
           'Japan', 'Russischtalige landen', 'Overige landen', 'China', 'Overige landen', 'Overige landen']


def overzicht(codes):
    result = {'Engelstalige landen': 0, 'Franstalige landen': 0, 'Duitstalige landen': 0,
              'Japan': 0, 'Russischtalige landen': 0, 'China': 0, 'Overige landen': 0, 'Fouten': 0}
    for code in codes:
        if len(code) != 13 or not code.isnumeric() or not (code[0:3] == '978' or code[0:3] == '979'):
            result['Fouten'] += 1
        else:
            t = 0
            for i in range(12):
                t += (3 if i % 2 == 1 else 1) * int(code[i])
            t = (10 - (t % 10)) % 10
            if int(code[-1]) == t:
                result[mapping[int(code[3])]] += 1
            else:
                result['Fouten'] += 1
    for key in result:
        print(f'{key}: {result[key]}')
