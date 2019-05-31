##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 
import pandas as pd
data=pd.read_csv('tbl0.tsv',delimiter='\t', encoding='utf-8')
data['ano'] = data._c3.apply(lambda x: x[:4])
print (data)