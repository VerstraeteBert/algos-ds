def gift_inschrijven(tuple_, dict_):
    if tuple_[0] in dict_:
        dict_[tuple_[0]] += tuple_[1]
    else:
        dict_[tuple_[0]] = tuple_[1]
    return dict_