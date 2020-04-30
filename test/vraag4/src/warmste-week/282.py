
def gift_inschrijven(Otuple, Odictionary):

	Odictionary[Otuple[0]] = Otuple[1] + Odictionary[Otuple[0]]

	return Odictionary