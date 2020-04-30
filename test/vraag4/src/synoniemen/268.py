def synoniemen(tekst, woordenboek):
  tekst2=[]
  lijst=tekst.split(' ')
  for el in lijst:
    if el in woordenboek:
      tekst2.append(woordenboek[el])
    else:
      tekst2.append(el)
  tekst3=' '.join(tekst2)
  return(tekst3)