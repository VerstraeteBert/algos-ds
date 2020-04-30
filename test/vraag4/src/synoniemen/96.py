def synoniemen(t, s):
    b = t.split(' ')
    l = len(b)
    g = ""
    for i in range(l):
        if b[i] in s:
            b[i] = s[b[i]]



    for i in range(l):
        g = g + b[i] + " "

    g = g.strip()
    return g