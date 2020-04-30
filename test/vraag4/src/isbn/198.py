def isISBN_13(code):
    if type(code)!=str or len(code)!=13 or not code.isdigit():
        return False
    if not(code[:3]=='978' or code[:3]=='979'):
        return False
    o=e=0
    for i in range(12): #de 11de index is x12
        if i%2==0: #index 0 komt overeen met x1
            o+=int(code[i])
        else: #index 1 komt overeen met x2
            e+=int(code[i])
    x13=(10-(o+3*e)%10)%10
    if x13==int(code[12]):
        return True
    return False

'''def overzicht(codes):
    groepen={}
    for i in range(11):
        groepen[i]=0
    for code in codes:
        landcode=int(code[4])
        if not isISBN_13(code):
            groepen[10]+=1
        else:
            groepen[landcode]+=1
    print('Engelstalige landen: {}'.format(groepen[1]+groepen[0]))
    print('Franstalige landen: {}'.format(groepen[2]))
    print('Duitstalige landen: {}'.format(groepen[3]))
    print('Japan: {}'.format(groepen[4]))
    print('Russischtalige landen: {}'.format(groepen[5]))
    print('China: {}'.format(groepen[7]))
    print('Overige landen: {}'.format(groepen[6]+groepen[8]+groepen[9]))
    print('Fouten: {}'.format(groepen[10]))'''

def overzicht(codes):
    types = ["Engelstalige landen", "Franstalige landen", "Duitstalige landen", "Japan", "Russischtalige landen", "China", "Overige landen", "Fouten"]

    overzicht = {}

    for type in types:
        overzicht[type] = 0
    for code in codes:
        if not isISBN_13(code):
            overzicht["Fouten"] += 1
        else:
            nr = code[3]
            if nr == "0":
                nr = "1"  #engelstalig
            elif nr in "689":
                nr = "7" #Overige landen
            elif nr == "7":
                nr = "6"
            type = types[int(nr)-1]
            overzicht[type] += 1

    for key in overzicht:
        print("{}: {}".format(key, overzicht[key]))