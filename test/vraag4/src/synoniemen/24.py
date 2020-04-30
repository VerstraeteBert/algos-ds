def synoniemen(zin, woordenboek):
        lijst = zin.split()
        for a in range(len(lijst)):
            if lijst[a] in woordenboek:
                lijst[a] = woordenboek[lijst[a]]
        nieuw = ''
        for a in lijst:
            nieuw += a + ' '
        return nieuw.strip()
