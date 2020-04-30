def synoniemen(zin, boek):
    lijst = zin.split(" ")
    nieuw = []
    for element in lijst:
        if element in boek:
            element= boek[element]
        nieuw.append(element)
    zin = " ".join(nieuw)
    return zin