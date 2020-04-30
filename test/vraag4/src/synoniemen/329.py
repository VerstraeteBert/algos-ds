def synoniemen(zin):
    woorden = {'straf': 'sanctie', 'stout': 'kwaadaardig', 'leerling': 'cursist', 'leraar': 'docent', 'school': 'troep',
               'knoeien': 'broddelen', 'kwaad': 'gebelgd', 'slecht': 'beroerd'}
    zin= zin.split()
    lengte= len(zin)
    for x in range(0,lengte):
        for y in woorden:
            if zin[x]== y:
                zin[x]= woorden[y]
    eind=' '.join(zin)
    print(eind)
ingave= input()
synoniemen(ingave)