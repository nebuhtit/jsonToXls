import pandas as pd
import datetime
pathToFile = '/Users/konstantin/PycharmProjects/remiind/dont_delete/test.xlsx'
xl = pd.read_excel(pathToFile, sheet_name=3, index_col=None)
d = pd.DataFrame(xl).to_dict()
nan = 'None'
names = eval(str(d['Имя']))
squares = eval(str(d['square']))
print(squares)
squares_kes = list(squares.keys())
print(squares)
l = []
l2 = []
for q in squares_kes:
    if squares[q] not in l:
        l.append(squares[q])
        l2.append(q)
    else:
        l2.append(q)