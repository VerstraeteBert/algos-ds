def synoniemen(tekst, woordenboek):
  woorden = ""
  for woord in tekst.split():
    if woord in woordenboek:
      woorden += woordenboek[woord] + " "
    else: 
      woorden += woord + " "
  return woorden[:-1]