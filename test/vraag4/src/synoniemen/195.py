def synoniemen(tekst, boek):
    nieuw = ''
    woorden = tekst.split()
    for sleutel in woorden:
        if sleutel in boek.keys():
            woord = boek.get(sleutel)
            nieuw += '{} '.format(woord)
        else:
            nieuw += '{} '.format(sleutel)
    return nieuw.strip()
        