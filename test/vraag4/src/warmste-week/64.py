def gift_inschrijven(sponser, giften):
  klas, bedrag = sponser
  if klas in giften:
    giften[klas] += bedrag
  else:
    giften[klas] = bedrag
  return giften