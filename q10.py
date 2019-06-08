##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 
import pandas as pd

df = pd.read_csv('tbl1.tsv', delimiter='\t')
group = df.groupby('_c0')
data = []

for i in group:
    letters = sorted(list(i[1]['_c4']))
    number = i[0]
    letters_string = str(letters[0])

    for j in range(1, len(letters)):
        letters_string += ',%s' % (str(letters[j]))

    data.append([number, letters_string])

df = pd.DataFrame(data=data, columns=['_c0', 'lista'])
print(df)
