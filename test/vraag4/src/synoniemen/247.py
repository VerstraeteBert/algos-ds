dictionary = {'straf': 'sanctie', 'stout': 'kwaadaardig', 'leerling': 'cursist','leraar': 'docent','school': 'troep','knoeien': 'broddelen','kwaad': 'gebelgd','slecht': 'beroerd'}

def synoniemen(zin, dic):
    output = ''
    for woord in zin.split():
        if dic.get(woord) != None:
            output += dic.get(woord) + ' '
        else:
            output += woord + ' '
            
    return output.strip()
