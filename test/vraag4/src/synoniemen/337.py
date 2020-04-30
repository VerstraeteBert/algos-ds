def synoniemen(tekst,dictionary):
    lijst = list(tekst.split( ))
    nieuw=""
    for i in lijst:
        if i in dictionary:
            nieuw += dictionary[i]
        if i not in dictionary:
            nieuw += i
        nieuw +=" "
        einde = nieuw.strip()
    return einde
