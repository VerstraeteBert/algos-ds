def verlaat_ploeg(naam, ploegnaam, dictionary):
    lijst = dictionary[ploegnaam]
    lijst.remove(naam)
    if lijst == []:
        del dictionary[ploegnaam]
    else:
        dictionary[ploegnaam] = lijst
    return dictionary

def vervoegt_ploeg(naam, ploegnaam, dictionary):
    if ploegnaam in dictionary:
        lijst = dictionary[ploegnaam]
        lijst.append(naam)
        dictionary[ploegnaam] = lijst
    else:
        lijst = [naam]
        dictionary[ploegnaam] = lijst
    return dictionary