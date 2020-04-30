def gift_inschrijven(info, boek):
    if info[0] in boek.keys():
        boek[info[0]] +=  info[1]
    else:
        boek[info[0]] = info[1]
    return boek