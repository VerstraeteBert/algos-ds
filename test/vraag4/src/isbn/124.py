
def isISBN13(code):
    if not(isinstance(code, str) and len(code) == 13 and code.isdigit()):
        return False
    if code[:3] not in ["978", "979"]:
        return False
    controle = 0
    for i in range[12]:
        if i%2:
            controle = controle + (3 * int(code[i]))
        else:
            controle = controle + int(code[i])
    nummer = controle%10
    nummer = (10 - nummer)%10
    return nummer == int(code[-1])
    
def overzicht(codes):
    verzameling = []
    for i in range(11):
        verzameling[i] = 0
    for code in codes:
        if not isISBN13(code):
            verzameling[10] = verzameling[10] + 1
        else:
            verzameling[int(code[3])] = verzameling[int(code[3])] + 1
    print("Engelstalige landen: {}".format(verzameling[0] + verzameling[1]))
    print("Franstalige landen: {}".format(verzameling[2]))
    print("Duitstalige landen: {}".format(verzameling[3]))
    print("Japan: {}".format(verzameling[4]))
    print("Russischtalige landen: {}".format(verzameling[5]))
    print("China: {}".format(verzameling[7]))
    print("Overige Landen: {}".format(verzameling[6] + verzameling[9] + verzameling[0]))
    print("Fouten: {}".format(verzameling[10]))
    
    