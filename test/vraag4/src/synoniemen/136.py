def synoniemen(x,y):
    a = x.split()
    i = 0
    while i < len(a):
        if a[i] in y:
           a[i] = y[a[i]]
        i += 1
    b= ' '.join(a)
    return b