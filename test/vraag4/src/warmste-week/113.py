def gift_inschrijven(sponsoring, giften):
  klas , gift = sponsoring
  if not klas in giften:
    giften[klas] = 0
  giften[klas] += gift
  return giften