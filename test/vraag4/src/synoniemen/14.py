import re

def synoniemen(zin,dict):
    pattern = re.compile(r'\b(' + '|'.join(dict.keys()) + r')\b')
    return pattern.sub(lambda x: dict[x.group()], zin)
