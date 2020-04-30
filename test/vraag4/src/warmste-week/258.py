def gift_inschrijven(tuple, dictionary):
    nieuwe_bedragen = dictionary
    if tuple[0] in dictionary:
        nieuwe_bedragen[tuple[0]] += tuple[1]
    else:
        nieuwe_bedragen[tuple[0]] = tuple[1]
    return nieuwe_bedragen

