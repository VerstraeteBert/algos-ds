def overzicht(codes):
    e = 0
    f = 0
    d = 0
    j = 0
    r = 0
    c = 0
    o = 0
    k = 0
    for i in codes:
        o = 0
        e = 0
        for i in str(code):
            if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                return False
        if len(str(code)) != 13:
            return False
        if type(code) != str:
            return False
        for i in range(len(code) - 1):
            if i%2 == 0:
                o += int(code[i])
            else:
                e += int(code[i])
        x1 = o + 3*e
        x1 %= 10
        x2 = 10 - x1
        x2 %= 10
        code = str(code)
        if x2 == int(code[-1]):
            return True
        return False
        if i.startswith('978') or i.startswith('979'):
            if i[3] == '0' or i[3] == '1':
                e += 1
            elif i[3] == '2':
                f += 1
            elif i[3] == '3':
                d += 1
            elif i[3] == '4':
                j += 1
            elif i[3] == '5':
                r += 1
            elif i[3] == '7':
                c += 1
            elif i[3] == '6' or i[3] == '8' or i[3] == '9':
                o += 1
        else:
            k += 1
    print('Engelstalige landen: '+str(e))
    print('Franstalige landen: '+str(f))
    print('Duitstalige landen: '+str(d))
    print('Japan: '+str(j))
    print('Russischtalige landen: '+str(r))
    print('China: '+str(c))
    print('Overige landen: '+str(o))
    print('Fouten: '+str(k))