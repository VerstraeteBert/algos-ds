def synoniemen(zin, dictionary):
  nieuwe_zin = ""
  nieuwe_lijst = []
  lijst = zin.split(" ")
  for i in range(len(lijst)):
    if(str(dictionary.get(lijst[i])) == "None"):
      nieuwe_lijst.append(lijst[i])
    else:
      nieuwe_lijst.append(str(dictionary.get(lijst[i])))
  nieuwe_zin = " ".join(nieuwe_lijst)
  return nieuwe_zin