def synoniemen(zin, bib):
	woorden = []
	for woord in zin.split():
		if woord in bib:
			woorden.append(bib[woord])
		else: 
			woorden.append(woord)
	return ' '.join(woorden)