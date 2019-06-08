##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
## 
import pandas as pd

df = pd.read_csv('tbl2.tsv', delimiter='\t')
data = []
c5_a = df['_c5a']
c5_b = df['_c5b']

for i, j in zip(c5_a, c5_b):
    data.append([i,j])

df = pd.DataFrame(data=data, columns=['_c5a', ''])
df = df.groupby('_c5a')

data = []
for i in df:
    sum_elements = sum(list(i[1]['']))
    label = i[0]
    data.append([label, sum_elements])

df = pd.DataFrame(data=data, columns=['_c5a', ''])
print(df)

