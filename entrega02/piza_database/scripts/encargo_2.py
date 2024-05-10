# -*- coding: utf-8 -*-
"""Encargo 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YFdpUi22f9EjklqDyynIfO45ohyiVXQa
"""

pip install pandas

import pandas as pd

df = pd.read_csv("/content/drive/MyDrive/datos.csv")

print (df)

print(df.dtypes)

print(df.head())

print(df.describe())

df_final = df.dropna(subset=['Incident_ID'], axis=0)

df_final = df.dropna(subset=['Date'], axis=0)

df_final = df.dropna(subset=['School'], axis=0)

df_final = df.dropna(subset=['City'], axis=0)

df_final = df.dropna(subset=['Summary'], axis=0)

df_final = df.dropna(subset=['State'], axis=0)

df_final = df.dropna(subset=['Targets'], axis=0)

print (df)

df_limpio = df.dropna()

print(df_limpio)

ciudades_frecuentes = df['City'].value_counts()

print(ciudades_frecuentes)

estados_frecuentes = df['State'].value_counts()

print(estados_frecuentes)

ciudad_estado_frecuente = df.groupby(['City', 'State']).size().sort_values(ascending=False)

print(ciudad_estado_frecuente)

ciudad_estado_frecuencia = df.groupby(['City', 'State']).size()

ciudad_estado_ordenado = ciudad_estado_frecuencia.sort_values(ascending=False)

top_50_ciudades_estados = ciudad_estado_ordenado.head(50)

df_top_50 = top_50_ciudades_estados.reset_index(name='repeticiones')

print(df_top_50)