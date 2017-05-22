# -*- coding: utf-8 -*-
"""
Created on Sun May 21 19:16:44 2017

@author: Berly Joaquin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def clean_data(dataframe, renda, bolsa, dict_renda=None):
    new_dataframe = pd.DataFrame(columns=['ano', 'idade'])
    new_dataframe['ano'] = dataframe['nu_ano']
    new_dataframe['idade'] = dataframe['nu_idade']
    new_dataframe['bolsa'] = dataframe[bolsa].str.lower()
    
    if dict_renda is None:
        dict_renda = { 'a': 1.5, 'b': 2.25, 'c': 3.75, 'd': 5.25, 'e': 8.0, 'f': 15.0, 'g': 30.0 }
    
    r = dataframe[renda].str.lower()
    
    new_dataframe['renda'] = r.map(dict_renda)
    

    return new_dataframe

dict_renda_2011 = { 'b': 1.5, 'c': 2.25, 'd': 3.75, 'e': 5.25, 'f': 8.0, 'g': 15.0, 'h': 30.0 }

df10 = clean_data(pd.read_csv('microdados_enade_2010.csv', encoding='latin1', delimiter=';'), 'QE_I5', 'QE_I10')
df11 = clean_data(pd.read_csv('microdados_enade_2011.csv', encoding='latin1', delimiter=';'), 'co_rs_s5','co_rs_s10', dict_renda_2011)
df12 = clean_data(pd.read_csv('microdados_enade_2012.csv' ,encoding='latin1', delimiter=';'), 'qe_i5', 'qe_i10')
df13 = clean_data(pd.read_csv('microdados_enade_2013.csv', delimiter=';'), 'co_rs_s7', 'co_rs_s10' )
df14 = clean_data(pd.read_csv('microdados_enade_2014.csv', delimiter=';', low_memory=False),  'qe_i8', 'qe_i11')

dfs = [df10, df11, df12, df13, df14]


df = pd.DataFrame()

df = df.append(dfs)

df.describe()


df.renda.unique()
df.boxplot(column='renda', by='ano')

df['renda'].hist(by=df['ano'])

ind= np.arange(len(df['bolsa']))
count_bolsa=df['bolsa'].value_counts()

x_axis= {'.','a','b','#','e','f','c','h','g','i','j','d','k'}
tam_x=np.arange(len(x_axis))
 plt.bar(tam_x, count_bolsa)
plt.xticks(tam_x, x_axis)
plt.show()