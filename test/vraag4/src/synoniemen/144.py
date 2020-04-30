def synoniemen(tekst, woordenboek):
    nieuw=''
    lijst=tekst.split()
    for i in range(len(lijst)):
        if lijst[i] in woordenboek:
            woord= woordenboek[lijst[i]]
            nieuw+=woord+' '
        else:
            nieuw += lijst[i] + ' '
    return nieuw[:-1]
