def histogram(stenen):
    histogram={}
    stenen.sort()
    for element in stenen:
        aantal=stenen.count(element)
        histogram[element]=aantal
    return histogram

def max_gelijk(stenen):
    max=0
    for element in stenen:
        aantal=stenen.count(element)
        if aantal>max:
            max=aantal

    return max

def is_FullHouse(stenen):
    trio=False
    duo=False
    for element in stenen:
        aantal=stenen.count(element)
        if aantal==3:
            trio=True
        if aantal==2:
            duo=True
    if trio==True and duo==True:
        return True
    else:
        return False