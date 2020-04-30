def gift_inschrijven(klas,data):
    sleutel = klas[0]
    waarde = float(klas[1])

    if sleutel in data:
        data[sleutel] = float(data[sleutel]) + waarde
    else:
        data[sleutel] = waarde


    return(data)