def synoniemen(tekst, woordenboek):
    vervang_tekst = ''
    lengte = 0
    while len(tekst) != 0:
        plaats = tekst.find(' ')
        if plaats == -1:
            woord = tekst
            tekst = tekst.lstrip(woord)
        else:
            woord = tekst[0: plaats]
        lengte += len(woord) + 1
        if woord in woordenboek:
            vervang_woord = woordenboek[woord]
            vervang_tekst += vervang_woord + ' '
        else:
            vervang_tekst += woord + ' '
        tekst = tekst[plaats+1:]
    return vervang_tekst.strip()