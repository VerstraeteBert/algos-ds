def synoniemen(zin, dictionary):
    lijst = zin.split()
    result = []
    for woord in lijst:
        if woord in dictionary:
            result.append(dictionary[woord])
        else:
            result.append(woord)
    return " ".join(result)

