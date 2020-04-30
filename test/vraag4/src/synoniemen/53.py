def synoniemen(zin,dictionary):
 lijst = zin.split()
 word = ""

 for i in range(len(lijst)):
   word = lijst[i]           
   if word in dictionary:           
     word = dictionary[word]        
     lijst[i] = word
 verwerktezin = " ".join(lijst)
 return verwerktezin

    
 


