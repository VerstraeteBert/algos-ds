def check(code):
  o = int(code[0]) + int(code[2]) + int(code[4]) + int(code[6]) + int(code[8]) + int(code[10])
  e = int(code[1]) + int(code[3]) + int(code[5]) + int(code[7]) + int(code[9]) + int(code[11])
  x13 = (10-(o + 3*e)%10)%10
  if(int(code[12]) == x13):
    return True
  else:
    return False
def overzicht(codes):
  engels = 0
  frans = 0
  duits = 0
  japans = 0
  rus = 0
  chinees = 0
  overig = 0
  fouten = 0
  for i in range(len(codes)):
    if(check(codes[i])):
      if((codes[i][3] == '0') or (codes[i][3] == '1')):
        engels += 1
      elif(codes[i][3] == '2'):
        frans += 1
      elif(codes[i][3] == '3'):
        duits += 1
      elif(codes[i][3] == '4'):
        japans += 1
      elif(codes[i][3] == '5'):
        rus += 1
      elif(codes[i][3] == '7'):
        chinees += 1
      else:
        overig += 1
    else:
      fouten +=1
  print("Engelstalige landen: " + str(engels))
  print("Franstalige landen: " + str(frans))
  print("Duitstalige landen: " + str(duits))
  print("Japan: " + str(japans))
  print("Russischtalige landen: " + str(rus))
  print("China: " + str(chinees))
  print("Overige landen: " + str(overig))
  print("Fouten: " + str(fouten))