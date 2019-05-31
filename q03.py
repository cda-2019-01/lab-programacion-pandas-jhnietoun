##
## Imprima el maximo de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 
import pandas as pd
data=pd.read_csv('tbl0.tsv',delimiter='\t', encoding='utf-8')
data=(data.groupby('_c1').max())["_c2"]
print (data)
