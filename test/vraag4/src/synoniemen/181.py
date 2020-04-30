def synoniemen(zin,woordenboek):
    code=''
    for woord in zin.split():
        if woord in woordenboek:
            code+=(woordenboek[woord])+' '
        else:
            code+=woord +' '
    code=code[:len(code)-1:]
    return code