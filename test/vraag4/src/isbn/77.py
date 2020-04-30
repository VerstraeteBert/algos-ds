def som_reeks(reeks):
    cijfers = [int(teken) for teken in reeks]
    return sum(cijfers)

def isISBN_13(isbn):
    if not type(isbn) is str:
        return False
    if len(isbn) != 13:
        return False
    if not isbn.isdigit():
        return False
    if isbn.find('978') != 0 and isbn.find('979') != 0:
        return False
    
    som_oneven = som_reeks(isbn[:12:2])
    som_even = som_reeks(isbn[1::2])
    controle = (10 - (som_oneven + 3 * som_even)%10) %10
    return int(isbn[12]) == controle
    
def overzicht(codes):
    land_codes = {"0" : "Engelstalige landen", "1" : "Engelstalige landen", "2" : "Franstalige landen",  \
    "3": "Duitstalige landen", "4": "Japan", "5": "Russischtalige landen", "7": "China", "6": "Overige landen", \
    "8": "Overige landen", "9": "Overige landen"}
    foutief = "Fouten"
    overzicht = {}
    for landtype in land_codes.values():
        overzicht[landtype] = 0
    overzicht[foutief] = 0
    for code in codes:
        if isISBN_13(code):
            overzicht[land_codes[code[3]]] += 1
        else:
            overzicht[foutief] += 1
    for landtype, aantal in overzicht.items():
        print("{}: {}".format(landtype, aantal))
        
