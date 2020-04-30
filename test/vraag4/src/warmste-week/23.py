#warmste week 
def gift_inschrijven(tup, dictionary):
    if tup[0] in dictionary:
        dictionary[tup[0]] += tup[1]
    else:
        dictionary[tup[0]] = tup[1]
    return dictionary