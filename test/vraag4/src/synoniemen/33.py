def synoniemen(zin, dictionary):
    n_zin = ''
    s_zin = zin.split(' ')
    for i in s_zin:
        if i in dictionary:
            woord = dictionary[i]
            n_zin += woord
            #print(dictionary[i], woord)
        else:
            n_zin += i
        n_zin += ' '
    return n_zin[:-1]
