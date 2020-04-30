def gift_inschrijven(tupel, dictionary):
 klas = tupel[0]
 bedrag = tupel[1]
 if klas in dictionary == False:
  dictionary[klas] = float(bedrag)
 else:
    currentvalue = str(dictionary.get(klas))
    dictionary[klas] = float(currentvalue.lstrip()) + float(bedrag)
 return dictionary