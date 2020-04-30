def synoniemen(zin, dict):
    woorden = zin.split(' ')
    nieuwe_zin = ''
    for woord in woorden:
        if woord in dict:
            nieuwe_zin += dict[woord] + ' '
        else:
            nieuwe_zin += woord + ' '
    return nieuwe_zin.strip()