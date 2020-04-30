def gift_inschrijven(donaties, giften):
  klas, gift = donaties
  tel = 0
  for klassen in giften:
    if klassen == klas:
      giften[klassen] += gift
      tel += 1
  if tel == 0:
    giften[klas] = gift
  return giften
    