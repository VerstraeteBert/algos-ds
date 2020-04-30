def isISBN_13(code):
    if len(code) != 13:
        return False
        
    if code[:3] != "978" and code [:3] != "979":
        return False
    even = code[::2]
    oneven = code[1::2]
    someven = 0
    somoneven = 0
    for i in range(6):
        cijfer = int(even[i])
        someven += cijfer
        cijfer = int(oneven[i])
        somoneven += cijfer
    controle = (10-(someven + 3 * somoneven) %10)%10

    return controle == int(even[6]