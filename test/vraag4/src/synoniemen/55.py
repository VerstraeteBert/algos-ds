import string
def synoniemen(zin,woordenboek):
    lijstzin= zin.split(' ')
    teller = 0
    teller2 = 0
    resultaat =''
    for item in lijstzin:
        item= item.strip(string.punctuation)
        lijstzin[teller] = item
        teller += 1
    for woord in lijstzin:
        if woord in woordenboek:
            vervanging = woordenboek[woord]
            lijstzin[teller2] = vervanging
        resultaat += lijstzin[teller2] + ' ' 
        teller2 +=1
    resultaat = resultaat.strip()
    return resultaat

