# -*- coding: utf-8 -*-
"""
Created on Sun May 21 19:16:44 2017

@author: Berly Joaquin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dict_bolsa_10_11_12 = {'a': 'ProUni Integral', 'b': 'ProUni Parcial', 'c': 'FIES', 'd':'ProUni Parcial e FIES', 'e':'Otra do estado', 'f':'Ofrecida pela própia instituição de ensino', 
              'g': 'Empresa, ONG, etc', 'h':'Financiamiento pela própia institução de ensino', 'i':'Financiamento pelo banco privado, etc', 'j':'Mais de um dos tipos de bolsa ou financiamento citados'}

dict_bolsa_13_14={'a': 'Nenhum, pois meu curso é gratuito', 'b':'Nenhum, embora meu curso não seja gratuito', 'c':'ProUni integral', 'd':'ProUni parcial, apenas', 'e':'FIES, apenas', 'f': 'ProUni Parcial e FIES', 'g':'Bolsa oferecida por governo estadual, distrital ou municipal', 'h' :'Bolsa oferecida pela própria instituição', 'i':'Bolsa oferecida por outra entidade (empresa, ONG, outra)', 'j' : 'Financiamento oferecido pela própria instituição', 'k': 'Financiamento bancário'}

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

p10=df10['bolsa'].str.lower()
df10['bolsa']=p10.map(dict_bolsa_10_11_12)

p11=df11['bolsa'].str.lower()
df11['bolsa']=p11.map(dict_bolsa_10_11_12)

p12=df12['bolsa'].str.lower()
df12['bolsa']=p12.map(dict_bolsa_10_11_12)

p13=df13['bolsa'].str.lower()
df13['bolsa']=p13.map(dict_bolsa_13_14)

p14=df14['bolsa'].str.lower()
df14['bolsa']=p14.map(dict_bolsa_13_14)




def13_tot=df13['bolsa'].value_counts(ascending=True)
def13_tot.plot.barh()



def14_tot=df14['bolsa'].value_counts(ascending=True)
def14_tot.plot.barh()




dfs = [df10, df11, df12, df13, df14]


df = pd.DataFrame()

df = df.append(dfs)

df.describe()


df.renda.unique()
df.boxplot(column='renda', by='ano')

df['renda'].hist(by=df['ano'])



