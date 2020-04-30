def verlaat_ploeg(verlaat,ploeg,dictionary):
    a= dictionary[ploeg]
    for i in range(len(a)):
        if a[i]== verlaat:
            a.remove(verlaat)
        else:
            a.append(verlaat)
    dictionary[ploeg]=a
    return dictionary
