def synoniemen(tekst, woordenboek):
    resultaat = ''
    tekst1 = tekst.split(' ')
    for woord in tekst1:
        if woord in woordenboek.keys():
            resultaat += woordenboek[woord] +' '

        else:
            resultaat += woord +' '

    return resultaat[:-1]       #laatste spatie verwijderen