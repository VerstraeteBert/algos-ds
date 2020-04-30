def synoniemen(tekst,dictionary):
    tekst = tekst.split()

    nieuwe =""
    for i in tekst:
        if i in dictionary:
            nieuwe += dictionary[i]
            nieuwe += ' '
        else:
            nieuwe += i
            nieuwe += ' '
    nieuwe = nieuwe.strip()
    return nieuwe