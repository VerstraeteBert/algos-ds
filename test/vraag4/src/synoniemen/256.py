def synoniemen(tekst, woordenboek):
  lijst=[]
  for woord in tekst.split():
    if woord in woordenboek:
      lijst.append(woordenboek[woord])
    else:
      lijst.append(woord)
  return " ".join(lijst)