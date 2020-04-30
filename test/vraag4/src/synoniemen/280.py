def synoniemen(tekst, woordenboek):
    nieuw = []
    tekst = tekst.split(' ')
    for i in tekst:
        if i in woordenboek:
            i = woordenboek[i]
            nieuw += [i]
        else:
            nieuw += [i]
    return " ".join(nieuw)
print(synoniemen('knoeien levert stoute leerlingen een straf op',{'straf': 'sanctie', 'stout': 'kwaadaardig', 'leerling': 'cursist', 'leraar': 'docent', 'school': 'troep', 'knoeien': 'broddelen', 'kwaad': 'gebelgd', 'slecht': 'beroerd'}))