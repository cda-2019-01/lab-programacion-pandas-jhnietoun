##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 
import pandas as pd
data=pd.read_csv('tbl0.tsv',delimiter='\t', encoding='utf-8')
data['suma'] = data['_c0']+data['_c2']
print (data)