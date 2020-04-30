
def synoniemen(zin, synoniemdictionary):

	zinlijst = zin.split(' ')

	for x in range(0,len(zinlijst)):
		if zinlijst[x] in synoniemdictionary:
			zinlijst[x] = synoniemdictionary[zinlijst[x]]

	zinlijst = ' '.join(zinlijst)

	return zinlijst
