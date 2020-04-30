def isISBN_13(code):
    o = 0
    e = 0
    if type(code) == str and len(code) == 13:
        for i in range(0,12,1):
            if code[i].isalpha():
                return False
            x = int(code[i])
            a = i + 1
            if a%2 == 0:
                e += x
            if a%2 == 1:
                o += x
        tot = (10 - (o + 3*e)%10)%10
        if code[12].isdigit() and tot == int(code[12]):
            return True
        else:
            return False
    else:
        return False
        
def overzicht(codes):
    en, fr, de, jap, rus, ch, over, fout = 0,0,0,0,0,0,0,0
    for code in codes:
        if isISBN_13(code) == True and code[0:3] == '979' or code[0:3] == '978':
            if code[3] == '0' or code[3] = '1':
                en += 1
            if code[3] == '2':
                fr += 1
            if code[3] == '3':
                de += 1
            if code[3] == '4':
                jap += 1
            if code[3] == '5':
                rus += 1
            if code[3] == '7':
                ch += 1
            if code[3] == '6' or code[3] == '8' or code[3] == '9':
                over += 1
            else:
                fout += 1
        else:
            fout += 1
    print("Engelstalige landen:",en
    #met dictionairies!!!!!!!!!!!