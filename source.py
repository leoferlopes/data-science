import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def clean_data(dataframe):
    new_dataframe = pd.DataFrame(columns=['ano', 'idade'])
    new_dataframe['ano'] = dataframe['nu_ano']
    new_dataframe['idade'] = dataframe['nu_idade']
    return new_dataframe

df08 = clean_data(pd.read_csv('microdados_enade_2008.csv', encoding='latin1', delimiter=';'))
df09 = clean_data(pd.read_csv('microdados_enade_2009.csv', encoding='latin1', delimiter=';'))
df10 = clean_data(pd.read_csv('microdados_enade_2010.csv', encoding='latin1', delimiter=';'))
df11 = clean_data(pd.read_csv('microdados_enade_2011.csv', encoding='latin1', delimiter=';'))
df12 = clean_data(pd.read_csv('microdados_enade_2012.csv' ,encoding='latin1', delimiter=';'))
df13 = clean_data(pd.read_csv('microdados_enade_2013.csv', delimiter=';'))
df14 = clean_data(pd.read_csv('microdados_enade_2014.csv', delimiter=';', low_memory=False))

dfs = [df08, df09, df10, df11, df12, df13, df14]


df = pd.DataFrame()

df = df.append(dfs)

df.describe()

df.boxplot(column='idade', by='ano')

df['idade'].hist(bins=5,by=df['ano'])