def synoniemen(tekst, dic):
    nieuw = ''
    tekst = tekst.split(' ')
    for woord in tekst:
        if woord in dic.keys():
            nieuw += dic[woord] + ' '
        else:
            nieuw += woord + ' '
    return nieuw.strip()