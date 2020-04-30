def synoniemen (zin, dictionary):
    lijst = zin.split(" ")
    correctie = ""
    for el in lijst:
        if el in dictionary:
            el = dictionary[el]
            correctie += el + " "
        else:
            correctie += el + " "
            
    return (correctie.rstrip())