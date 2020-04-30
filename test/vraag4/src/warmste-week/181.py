def gift_inschrijven(tweetal, woordenboek):
  if woordenboek.get(tweetal[0]) == None:
    woordenboek[tweetal[0]] = tweetal[1]
  else:
    woordenboek[tweetal[0]] += tweetal[1]
  return woordenboek