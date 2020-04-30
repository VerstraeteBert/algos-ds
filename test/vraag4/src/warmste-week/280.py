def gift_inschrijven(param1, param2):
    if param1[0] in param2.keys():
        param2[param1[0]] += param1[1]
    else:
        param2.update({param1[0]: param1[1]})
        
    return param2