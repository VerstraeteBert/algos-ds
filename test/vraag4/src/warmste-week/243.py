def gift_inschrijven(tup, dic):
  klas= tup[0]
  bedrag= tup[1]
  if klas in dic:
    vorig= dic[klas]
    nieuw= vorig + bedrag
    dic[klas]= nieuw
  else:
    dic[klas]= bedrag
  
  return dic

