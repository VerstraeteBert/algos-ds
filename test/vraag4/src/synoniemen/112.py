def synoniemen(sen: str, d: dict):
    sen_list = sen.split()
    new_str = ""
    for i in sen_list:
        if i in d:
            new_str += " " + d[i]
        else:
            new_str += " " + i

    return new_str.lstrip()