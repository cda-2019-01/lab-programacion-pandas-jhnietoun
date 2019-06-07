##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 
import pandas as pd
data=pd.read_csv('tbl0.tsv',delimiter='\t', encoding='utf-8')
c1=data['_c1']
c2=data['_c2']
dict_data={}

for i,j in zip(c1,c2):
    if i in dict_data:
        dict_data[i].append(j)
    else:
        dict_data[i]=[j]
        
label=sorted(dict_data)

arreglo=[]
for i in label:
    var=sorted(dict_data[i])
    value=str(var[0])
    for j in range(1,len(var)):
        value+=':%s'%str(var[j])
    arreglo.append(value)

result=[]

for i,j in zip (label,arreglo):
    result.append([i,j])

df=pd.DataFrame(result, columns = ['_c0', 'lista'])

print(df)
    
