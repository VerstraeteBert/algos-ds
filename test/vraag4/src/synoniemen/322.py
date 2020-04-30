def synoniemen(zin, synoniemen):
  woorden = []
  for woord in zin.split():
    if woord in synoniemen:
      woorden.append(synoniemen[woord])
    else:
      woorden.append(woord)
  return " ".join(woorden)