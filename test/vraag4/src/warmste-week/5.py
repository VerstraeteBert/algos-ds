def gift_inschrijven(tuple, dict):
    if tuple[0] in dict:
        # print('ok')
        dict[tuple[0]] = dict[tuple[0]] + tuple[1]
    else:
        dict[tuple[0]] = tuple[1]
    return dict

# print(gift_inschrijven(('5WWI', 78.33),{'6WWI': 64.87, '6BI': 71.63, '5BI': 26.39, '5WWI': 82.68}))