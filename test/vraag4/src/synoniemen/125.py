def synoniemen(text, dictionary):
    woorden = text.split()
    for i in range(len(woorden)):
        if woorden[i] in dictionary:
            woorden[i] = dictionary[woorden[i]]
    return " ".join(woorden)