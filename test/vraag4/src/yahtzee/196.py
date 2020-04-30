def histogram(dobbels):
    verzameling={}
    for i in range(11):
        if dobbels.count(i)>0:
            aantal=dobbels.count(i)
            verzameling[i]=aantal
    return verzameling

def max_gelijk(dobbels):
    verzameling=histogram(dobbels)
    max=0
    for i in verzameling:
        if verzameling[i]>max:
            max=verzameling[i]
    return max
def is_FullHouse(dobbels):
    full=False
    verzameling=histogram(dobbels)
    if len(verzameling) !=2:
        return False
    else:
        for i in verzameling:
            if verzameling[i] == 2:
                full=True
    return full

