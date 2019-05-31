##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 
import pandas as pd
data=pd.read_csv('tbl1.tsv',delimiter='\t', encoding='utf-8')
data=data.apply(lambda x: x.astype(str).str.upper())
data=data ['_c4'].unique()
print (sorted (data))