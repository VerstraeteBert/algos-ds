def gift_inschrijven(t,wb):
  klas=t[0]
  bedrag=t[1]
  if klas in wb:
    wb[klas]=wb[klas]+bedrag
  else:
    wb[klas]=bedrag
  return(wb)
