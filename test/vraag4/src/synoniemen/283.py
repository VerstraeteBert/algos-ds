def synoniemen(tekst, vervanging):
    woorden = tekst.lower().split()
    for i in range(len(woorden)):
        if woorden[i] in vervanging:
            woorden[i] = vervanging[woorden[i]]
    return " ".join(woorden)