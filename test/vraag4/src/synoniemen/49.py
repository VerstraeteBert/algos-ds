def synoniemen(tekst, woordenboek):
    t = tekst.split(' ')
    for i in woordenboek:
        for j in range(len(t)):
            if i == t[j]:
                t.remove(t[j])
                t.insert(j, woordenboek[i])
    z = ' '.join(t)
    return z
  