def synoniemen(zin, synoniem):
    lijst = zin.split(' ')
    nieuwe_zin = ''
    for words in lijst:
        if words in synoniem:
            nieuwe_zin += synoniem[words] + ' '
        else:
            nieuwe_zin += words +' '
    return nieuwe_zin[:-1]