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