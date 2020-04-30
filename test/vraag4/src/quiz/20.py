#quiz
def verlaat_ploeg(naam, ploeg, dick):
    for el in dick:
        if naam in dick[el]:
            plaats = dick[el].index(naam)
            dick[el].pop(plaats)#dit verwijdert het element op de aangegeven plaats
    if dick[ploeg] == []:
        del(dick[ploeg])
    return dick  
def vervoegt_ploeg(naam, ploeg, dick):
    if ploeg in dick.keys():
        dick[ploeg] += [naam]
    else:
        dick[ploeg] = [naam]
    return dick