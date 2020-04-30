def isISBN_13(code):
    try:
        if not (code[:3] == '978' or code.startswith('979', 0 , 3)):
            return False
        if len(code) != 13:
            return False

        som1 = 0
        for i in code[:-1:2]:
            som1 += int(i)

        som2 = 0
        for i in code[1:-1:2]:
            som2 += int(i)

        controle = (10 - (som1 + 3 * som2) % 10) % 10
        if int(code[-1]) == controle:
            return True

        return False
    except TypeError:
        return False
    except ValueError:
        return False


def overzicht(codes):
    tabel = {
        'Engelstalige landen' : 0,
        'Franstalige landen' : 0,
        'Duitstalige landen' : 0,
        'Japan' : 0,
        'Russischtalige landen' : 0,
        'China' : 0,
        'Overige landen' : 0,
        'Fouten' : 0
    }
    ident = {
        'Engelstalige landen': [0, 1],
        'Franstalige landen': [2],
        'Duitstalige landen': [3],
        'Japan': [4],
        'Russischtalige landen': [5],
        'China': [7],
        'Overige landen': [6,8,9]
    }
    for isbn in codes:
        if isISBN_13(isbn):
            for key in ident:
                if int(isbn[3]) in ident[key]:
                    tabel[key] += 1
        else:
            tabel['Fouten'] += 1

    for key, i in tabel.items():
        print("{}: {}".format(key,i))
