
#importing libraries
import pandas as pd
import numpy as np

#reading the txedges.dat
col_names=['txID', 'in_addr', 'out_addr', 'weight'] 
df = pd.read_csv('txedges.dat',sep='\t',names=col_names, header=None)

lis_t=[] 
for i in range(len(df)):
  temp=[]
  temp.append(df['in_addr'][i])
  temp.append(df['out_addr'][i])
  lis_t.append(temp)
  
for j in range(len(lis_t)):
  if lis_t[j][0]==lis_t[j][1]:
    lis_t.remove(lis_t[j])
    
#Example of dict
#dic_t = {1: [2], 3: [1], 5: [4]}

dic_t={}
for k,v in lis_t:
  dic_t.setdefault(v,[]).append(k)
for i in dic_t:
  dic_t[i]=list(set(dic_t[i]))

#Adjacency Matrix
mat=[]
for i in range(43000):
  mat.append([0 for j in range(43000)])
for i in range(len(df)):
  if (df['in_addr'][i]==df['out_addr'][i]):
    print("Same vertex %d and %d" % (df['in_addr'][i],df['in_addr'][i]))
  mat[df['in_addr'][i]][df['out_addr'][i]]=1
  mat[df['out_addr'][i]][df['in_addr'][i]]=1


 