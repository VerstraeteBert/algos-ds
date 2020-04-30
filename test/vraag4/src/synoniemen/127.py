def synoniemen(zin_str, wb_dict):
        zin_list = zin_str.split(" ")
        for index, woord in enumerate(zin_list):
                if woord in wb_dict.keys():
                        zin_list[index] = wb_dict[woord]
        return " ".join(zin_list)
