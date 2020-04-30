def synoniemen(tekst, woordenboek):
    nieuw = ""
    tekst_nieuw = tekst.split()
    for woord in tekst_nieuw:
        if woord in woordenboek:
            nieuw += str(woordenboek[woord]) + " "
        else:
            nieuw += str(woord)  + " "
    return nieuw[:-1]



print(synoniemen('knoeien levert stoute leerlingen een straf op',{'straf': 'sanctie', 'stout': 'kwaadaardig', 'leerling': 'cursist', 'leraar': 'docent', 'school': 'troep', 'knoeien': 'broddelen', 'kwaad': 'gebelgd', 'slecht': 'beroerd'}))
