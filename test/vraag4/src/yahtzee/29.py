def histogram(list1):
    waarden = {}
    for i in list1:
        if i in waarden:
            waarden[i] += 1
        else:
            waarden[i] = 1
    return waarden

def max_gelijk(list1):
    waarden = histogram(list1)
    maxi = max(waarden, key=waarden.get)
    return waarden[maxi]
def is_FullHouse(list1):
    waarden = histogram(list1)
    if max_gelijk(list1) == 3:
        if len(waarden) == 2:
            return True
        else:
            return False
    else:
        return False
