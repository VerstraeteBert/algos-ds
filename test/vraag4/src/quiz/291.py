
def verlaat_ploeg (naam,ploeg,dictionary):
    namen = dictionary[ploeg]
    namen.remove(naam)
    dictionary[ploeg] = namen
    if len(dictionary[ploeg]) < 1:
        del dictionary[ploeg]

    return dictionary
    
def vervoegt_ploeg (naam, ploeg, dictionary):
    if ploeg in dictionary:
        namen = dictionary[ploeg]
        namen.append(naam)
        dictionary[ploeg] = namen
    else:
        dictionary[ploeg] = [naam]

    return dictionary