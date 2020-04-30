def gift_inschrijven(tuple,dictionary):
    nieuw = 0
    for i in dictionary.keys():

        if i == tuple[0]:
            dictionary[i] += tuple[1]
            nieuw += 1
    if nieuw == 0:
        dictionary[tuple[0]] = tuple[1]
    return dictionary