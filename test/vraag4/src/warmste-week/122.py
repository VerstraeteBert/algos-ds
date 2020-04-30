def gift_inschrijven(klas_en_bedrag_tuple, giften_dict):
        if klas_en_bedrag_tuple[0] in giften_dict.keys():
                giften_dict[klas_en_bedrag_tuple[0]] += klas_en_bedrag_tuple[1]
        else:
                giften_dict.update({klas_en_bedrag_tuple[0]: klas_en_bedrag_tuple[1]})
        return giften_dict

print(gift_inschrijven(('5WWI', 78.33),{'6WWI': 64.87, '6BI': 71.63, '5BI': 26.39, '5WWI': 82.68}))
