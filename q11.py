##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
import pandas as pd

df = pd.read_csv('tbl2.tsv', delimiter='\t')
group = df.groupby('_c0')
data = []

for i in group:
    c5_a = list(i[1]['_c5a'])
    c5_b = list(i[1]['_c5b'])
    number = i[0]
    sent = False
    new_list = [c5_a, c5_b]
    new_list = zip(*[x for x in new_list])
    new_list = sorted([tuple(x) for x in new_list])
    string_result = ''

    for j in new_list:
        if sent == False:
            string_result += '%s:%s' % (str(j[0]), str(j[1]))
            sent = True
        else:
            string_result += ',%s:%s' % (str(j[0]), str(j[1]))
        

    data.append([number, string_result])

df = pd.DataFrame(data=data, columns=['_c0', 'lista'])
print(df)
