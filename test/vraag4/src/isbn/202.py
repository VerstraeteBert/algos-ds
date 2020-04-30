def overzicht(codes):
    aantal = len(codes)
    eng = fr = duit = jap = rus = chin = over = fout = 0
    for teller in range(0,aantal):
        code = codes[teller]
        lengte = len(code)
        o = e = 0

        for count in range(0,lengte-1):
            if count%2 == 0:
                o += int(code[count])
            else:
                e += int(code[count])
        contro = code[lengte-1]
        x13 = (10-(o+3*e)%10)%10
        if(x13 == int(contro)):
            doorgaan = 1
        else:
            doorgaan = 0

        start = code[0:3]
        if ((start == '978') or (start == '979')) and doorgaan == 1:
            land = code[3]
            if(land in '01'):
                eng += 1
            elif(land in '2'):
                fr += 1
            elif(land in '3'):
                duit += 1
            elif(land in '4'):
                jap += 1
            elif(land in '5'):
                rus += 1
            elif(land in '7'):
                chin += 1
            elif(land in '689'):
                over += 1
        else:
            fout += 1

    print('Engelstalige landen:', eng)
    print('Franstalige landen:', fr)
    print('Duitstalige landen:', duit)
    print('Japan:', jap)
    print('Russischtalige landen:', rus)
    print('China:', chin)
    print('Overige landen:', over)
    print('Fouten:', fout)
