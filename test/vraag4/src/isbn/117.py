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
    return controle == int(isbn[12]), 
    
    
def overzicht (codes):
    dict = engels, frans, duits, jap, rus, chin, overig, fout = 0,0,0,0,0,0,0,0
    engelse, franse, duitsers, jappen, russen, chinesen, overige, fouten = 'Engelstalige landen: ', 'Franstalige landen: ', 'Duitstalige landen: ', 'Japan: ', 'Russischtalige landen: ', 'china: ', 'overige landen: ', 'fouten: '
    for nummer in code:
        check = isISBN_13(nummer)