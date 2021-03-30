import pandas as pd
from pprint import pprint
import tkinter
import json
import openpyxl

j = [
    {
        'cub': 1,
        'uch': 'a',
        'who': {'first': 'vasia', 'saecond': 'vasiliev'},
        'time': {'start': '01.02.03', 'finish': '02.03.05'}
    },
    {
        'cub': 2,
        'uch': 'b',
        'who': {'first': 'Ivan', 'saecond': 'Ivanov'},
        'time': {'start': '01.07.03', 'finish': '02.03.20'}
    }
]

v = {"map":{
    "cubes":{
        "uches":{
            "who":{"who_first":"who_first", 'who_second':'who_second'},
            'time': {'start': 'start', 'finish': 'finish'}
        }
    }
},

    "1": {"cub1": {

        'a': {
            'who': {'first': 'vasia', 'saecond': 'vasiliev'},
            'time': {'start': '01.02.03', 'finish': '02.03.05'}

        }}

    },
    "2": {"cub2": {

        'b': {
            'who': {'first': 'Ivan', 'saecond': 'Ivanov'},
            'time': {'start': '01.07.03', 'finish': '02.03.20'},
            'info':{'note':'qwery', 'ura':'343'}

        },
        'c': {
            'who': {'first': 'Evgen', 'saecond': 'Molod'},
            'time': {'start': '01.07.34', 'finish': '02.03.20'}
        }

    },
        "3":{
            'c':{}

        }

    }

}


# xl = pd.read_excel('exemple.xlsx', index_col=0)
# print(xl)
# dxl = xl.to_dict()
# pprint(dxl)
#
# element = list(dxl['start'].values())
# dxl['start'][' u1'] = 'kek'
# print(element)
# print(dxl)
# pd.DataFrame(dxl).to_excel('result.xlsx')
def dictToList(dict):
    l = []
    L = []
    for q in v:
        d0 = v[q]
        print(d0)
        for w in d0:
            d1 = d0[w]
            print(d1)
            for e in d1:
                d2 = d1[e]
                print(d2)
                print(e)
                l = [q, w, e]
                print(l)
                for r in d2:
                    d3 = d2[r]
                    for t in list(d3.values()):
                        l.append(t)
                    print(d3)
                    print(l)
                L.append(l)
    return L


list = dictToList(v)
print(")", list)

df = pd.DataFrame(list)

print(df)

df.to_excel('result.xls')
