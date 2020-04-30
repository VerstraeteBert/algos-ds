def synoniemen(tekst, woordenboek):
    tekstlijst = tekst.split(' ')
    for index, woord in enumerate(tekstlijst):
        try:
            tekstlijst[index] = woordenboek[woord]
        except KeyError:
            continue
    return ' '.join(tekstlijst)


print(synoniemen('knoeien levert stoute leerlingen een straf op',
                 {'straf': 'sanctie', 'stout': 'kwaadaardig', 'leerling': 'cursist', 'leraar': 'docent',
                  'school': 'troep', 'knoeien': 'broddelen', 'kwaad': 'gebelgd', 'slecht': 'beroerd'}))
