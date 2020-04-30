def synoniemen(zin, boek):
  woorden = []
  for woord in zin.split():
    if woord in boek:
      woorden.append(boek[woord])
    else:
      woorden.append(woord)
  return " ".join(woorden)