def synoniemen(zin, dict):
    elementen = zin.split()
    vervanging = ''
    for woord in elementen:
        if woord in dict:
            synoniem = dict[woord]
            vervanging += synoniem + ' '
        else:
            vervanging += woord + ' '
    return vervanging[:-1]