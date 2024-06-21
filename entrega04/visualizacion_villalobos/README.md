# Visualización atómica
#### Antonia Villalobos

## Selección de datos
Para la visualización de datos sobre incidentes de tiroteos se utilizó un archivo CSV: incidentes-new.csv. Este archivo contiene información limpia acerca de tiroteos recopiladas desde el año 2018. Los datos detallan el incidente, día, mes, año, escuela, víctimas fatales, heridos, Estado, ciudad, nivel escolar, si ocurrio durante clases, fuera o dentro del establecimiento, lugar,duración. Para hacer visualizaciones se seleccionaron datos que pueden ser útiles y coherentes para nuestra hipótesis. Se seleccionaron los datos acerca del Estado en dónde ocurrieron los incidentes, el nivel escolar y si ocurrieron dentro o fuera del establecimiento educacional, especificando el lugar. 

## Proceso de Visualización
Para hacer las visualizaciones se utilizó la biblioteca seaborn en Python, porque facilita la creación de gráficos y mapas de calor. Opté por representar los datos a través de gráficos de conteo por Estado, también un gráfico de barras agrupadas para 'Estado' y 'Nivel escolar', y un mapa de calor basado en la relación entre la ubicación, si fue dentro o fuera del establecimiento, y el lugar.

### Codificación de las variables incorpordas:

Primero subi el archivo incidents-new.csv a Colab. 

Para instalar y cargar las bibliotecas necesarias codifiqué: **!pip install seaborn** y en otra celda codifiqué: 

**import pandas as pd**

**import matplotlib.pyplot as plt**

**import seaborn as sns**

Para cargar los datos desde el archivo CSV usé el código:
**datos = pd.read_csv('/content/incidents-new.csv')**
y para explorar los datos:
**datos.head()**

Para crear las visualizaciones, primero cree un gráfico de conteo por nivel escolar: 

**plt.figure(figsize=(10, 6))
sns.countplot(x='School_Level', data=datos)
plt.title('Número de Incidentes por Nivel Escolar')
plt.xlabel('Nivel Escolar')
plt.ylabel('Número de Incidentes')
plt.xticks(rotation=45)
plt.show()**

Luego cree y guardé un gráfico de barras agrupadas para 'Estado' y 'Nivel escolar'

**plt.figure(figsize=(20, 10))
sns.countplot(data=datos, x='State', hue='School_Level')
plt.title('Relación entre Estado y Nivel Escolar')
plt.xlabel('Estado')
plt.ylabel('Número de Incidentes')
plt.xticks(rotation=90)
plt.legend(title='Nivel Escolar')
plt.savefig('/content/relacion_estado_nivel_escolar.png')
plt.show()**

Luego, para crear el mapa de calor, cree una tabla de contingencia entre 'Location' y 'Location_Type' y con esa tabla cree el mapa de calor.

**tabla_contingencia = pd.crosstab(datos['Location'], datos['Location_Type'])**

**plt.figure(figsize=(14, 8))
sns.heatmap(tabla_contingencia, annot=True, fmt='d', cmap='YlGnBu')**

**plt.title('Mapa de Calor de la Relación entre Location y Location_Type')
plt.xlabel('Location_Type')
plt.ylabel('Location')**

**plt.show()**

Finalmente, guardé el mapa de calor y el gráfico de conteo por nivel escolar como archivo PNG. El gráfico de barras agrupadas lo guardé altiro. 

**plt.figure(figsize=(14, 8))
sns.heatmap(tabla_contingencia, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Mapa de Calor de la Relación entre Location y Location_Type')
plt.xlabel('Location_Type')
plt.ylabel('Location')
plt.savefig('/content/heatmap_location_vs_location_type.png')**

**plt.figure(figsize=(10, 6))
sns.countplot(x='School_Level', data=datos)
plt.title('Número de Incidentes por Nivel Escolar')
plt.xlabel('Nivel Escolar')
plt.ylabel('Número de Incidentes')
plt.xticks(rotation=45)
plt.savefig('/content/numero_incidentes_nivel_escolar.png')
plt.show()** 


## Ejemplos de preguntas que pueden responder las visualizaciones

1. ¿Cuál es el estado con el mayor número de incidentes en el nivel escolar secundario?

2. ¿Qué tipo de ubicación tiene más incidentes en general (por ejemplo, dentro de la escuela, fuera de la escuela)?

3. ¿Hay alguna ubicación específica (por ejemplo, biblioteca, estacionamiento) que se destaque por tener un alto número de incidentes?

4. ¿Qué lugar es el más común en este tipo de incidentes, cuando ocurren dentro del establecimiento?