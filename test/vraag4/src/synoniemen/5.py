def synoniemen(tekst, synoniemenwoordenboek):
    woord = ''
    zin = ''
    for i in tekst:
        if i == ' ':
            if woord in synoniemenwoordenboek:
                woord = synoniemenwoordenboek[woord]
            if zin != '':
                zin += ' '+woord
            else:
                zin += woord
            woord = ''
        else:
            woord += i
    if woord in synoniemenwoordenboek:
        woord = synoniemenwoordenboek[woord]
    return zin+' '+woord


# print(synoniemen('knoeien levert stoute leerlingen een straf op',{'straf': 'sanctie', 'stout': 'kwaadaardig', 'leerling': 'cursist', 'leraar': 'docent', 'school': 'troep', 'knoeien': 'broddelen', 'kwaad': 'gebelgd', 'slecht': 'beroerd'}))
