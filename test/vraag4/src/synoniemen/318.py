def synoniemen(zin, data):
    lijst = list(zin.split())
    for i in range(len(lijst)):
        if lijst[i] in data:
            zin = zin.replace(lijst[i], data[lijst[i]])

    return (zin)