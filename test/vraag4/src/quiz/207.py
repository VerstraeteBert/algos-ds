def verlaat_ploeg(deelnemer, ploeg, inschrijvingen): #niet controleren of hij er in zat
    namen_array = inschrijvingen[ploeg]
    namen_array.remove(deelnemer)
    inschrijvingen[ploeg] = namen_array
    if inschrijvingen[ploeg] ==[]:
        inschrijvingen.pop(ploeg)

    return inschrijvingen


def vervoegt_ploeg(deelnemer, ploeg,inschrijvingen):
    if ploeg in inschrijvingen:
        namen_array = inschrijvingen[ploeg]
        namen_array.append(deelnemer)
        inschrijvingen[ploeg] = namen_array
    else:
        array = []
        array.append(deelnemer)
        inschrijvingen[ploeg] = array
    return inschrijvingen




#print(verlaat_ploeg('Tom','Sinbox',{'Sinbox': ['An', 'Tom', 'Griet'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))
#print(vervoegt_ploeg('Els','Sinbox',{'Sinbox': ['An', 'Griet'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))
#print(vervoegt_ploeg('Fien','Levies',{'Sinbox': ['An', 'Griet', 'Els'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))
#print(verlaat_ploeg('Fien','Levies',{'Sinbox': ['An', 'Griet', 'Els'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))