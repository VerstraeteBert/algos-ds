def synoniemen(zin,dictionary):
    
    zin_lijst = zin.split(" ")
    for element in zin_lijst:
        if element in dictionary.keys():
            index = zin_lijst.index()
            zin_lijst[index] = dictionary[element]

    new_string = ""
    for i in zin_lijst:
        new_string += i