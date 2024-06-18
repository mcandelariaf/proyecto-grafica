# -*- coding: utf-8 -*-
"""Encargo 4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZLWD1DMBSkaKDAck7J7Y7ivbWeCUqQ9K
"""

pip install pandas openpyxl

import pandas as pd


excel_file = '/content/drive/MyDrive/Colab Notebooks/datos para encargo 4.xlsx'


df = pd.read_excel(excel_file)


csv_file = 'datos para encargo 4.csv'
df.to_csv(csv_file, index=False)

print("Archivo convertido y guardado como {csv_file}")

import pandas as pd


data = pd.read_csv('datos para encargo 4.csv')


print(data.head())

import pandas as pd

# Cargar los datos desde el archivo CSV
data = pd.read_csv('datos para encargo 4.csv')

# Verificar que los datos se cargaron correctamente (opcional)
print(data.head())

# Agrupar los datos por año y realizar los cálculos
# Use the actual column names from your DataFrame
summary = data.groupby('Year').agg(
    incidents=('Incident_ID', 'count'),
    total_victims_killed=('Victims_Killed', 'sum'),
    total_victims_wounded=('Victims_Wounded', 'sum')
).reset_index()

# Mostrar el resumen
print(summary)

# Guardar el resumen en un archivo CSV
summary.to_csv('resumen_incidentes.csv', index=False)

!pip install seaborn

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
summary = pd.read_csv('resumen_incidentes.csv')


# Reformatear los datos para que seaborn pueda manejar múltiples series
summary_melted = pd.melt(summary, id_vars=['Year'],
                         value_vars=['incidents', 'total_victims_killed', 'total_victims_wounded'],
                         var_name='Category', value_name='Count')

# Verificar los datos reformateados (opcional)
print(summary_melted.head())

# Crear el gráfico de dispersión combinado
plt.figure(figsize=(12, 8))
sns.lineplot(data=summary_melted, x='Year', y='Count', hue='Category', style='Category')

# Ajustar el título y las etiquetas
plt.title('Incidents, Victims Killed, and Victims Wounded per Year')
plt.xlabel('Year')
plt.ylabel('Count')

# Mostrar el gráfico
plt.show()