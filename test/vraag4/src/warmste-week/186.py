def gift_inschrijven(tuple, dictionary):
    klas = tuple[0]
    bedrag = tuple[1]
    if klas in dictionary:
        dictionary[klas] += bedrag      # hierbij bestaat de klas al in de dictionary en wordt het bedrag opgeteld bij de bijhorende waarde van de klas
    else:
        dictionary[klas] = bedrag       # hier wordt de key van de respectievelijke klas aangemaakt en de z'n value meegegeven
    return dictionary

