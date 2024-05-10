# Proceso de limpieza de datos de Antonia Villalobos
Para el proyecto, utilicé una base de datos de  [Mother Jones Investigation](https://www.motherjones.com/politics/2012/12/mass-shootings-mother-jones-full-data/) porque tiene datos completos de tiroteos en Estados Unidos. El documento especifica los tiroteos ocurridos, el Estado en dónde ocurrieron y el año. También tiene información acerca de los tiradores, su edad, si consiguió el arma legalemente o no, y si tenia problemas de salud mental. Elegí esta base de datos porque creo que permite tener un panorama completo acerca de los incidentes de tiroteos en Estados Unidos y es útil para nuestro análisis. 

### 1. Importar la base de datos a Colab
Pasé de archivo Excel a CSV la base de datos de Mother Jones Investigation y le cambié el nombre a **tiroteos**. 
La importé a Colab y luego usé el código: **import pandas as pd** 
para cargar la base de datos

Luego definí el documento:

 **tiroteos = pd.read_csv("tiroteos.csv")**

Para poder ver las primeras filas de la base de datos codifiqué: **print(tiroteos.head())**

Ahí ya había cargado mi base de datos inicial, después solo necesitaba limpiarla y filtrar la información que necesitaba.

### 2. Filtrar las columnas necesarias

La base de datos aborda tiroteos desde 1982 hasta 2023, y especifica: caso, locación, resumen, muertos, heridos, total de víctimas, lugar, edad del tirador, antecedentes de problemas de salud mental, detalles de salud mental, armas obtenidas legalmente, dónde obtuvieron el arma, tipo de arma, detalles del arma, raza del tirador, género del tirador, fuentes de salud mental, latitud, longitud, tipo de tiroteo, año. 

Como nuestra **hipótesis** es: La razón detrás de la desproporcional diferencia en la cantidad de tiroteos escolares entre los estados con más incidentes versus aquellos con menos en Estados Unidos, en el contexto del alza de estos incidentes en los últimos seis años, recae en la cultura de la posesión de armas, la laxitud de las leyes y la falta de medidas de prevención.

Filtré las columnas necesarias para poder trabajar y demostrar nuestra hipótesis, para eso definí mi nueva base de datos con las columnas que necesito: 

**tiroteos_limpios = tiroteos[["case", "location", "fatalities", "injured", "total_victims",    "age_of_shooter", "gender", "prior_signs_mental_health_issues", "mental_health_details", "weapons_obtained_legally","year"]]**

Estas son: casos, lugar, muertos, heridos, total de víctimas, edad del tirador, género, antecedentes de problemas de salud mental, detalles de salud mental, armas obtenidas legalmente, año. 

### 3. Filtrar los datos desde el año 2017 en adelante
Como necesitamos datos de los últimos 6 años, filtré los datos desde el año 2017 en adelante. Para eso definí que la base de datos limpia debía tener ese rango usando este codigo: 

**tiroteos_limpios = tiroteos_limpios[tiroteos_limpios["year"] >= 2017]**

Después escribí el código: 
**print(tiroteos_limpios.head())**
para poder ver las primeras filas de la base de datos limpia

### 4. Guardar la nueva base de datos
Para guardar los datos limpios en un nuevo archivo CSV llamado "tiroteos_limpios.csv" utilicé el código:

**tiroteos_limpios.to_csv("tiroteos_limpios.csv", index=False)**

Después de que se limpieraron los datos y tenemos nuestra nueva base de datos, la descargamos y trabajamos con ella. 

### Ejemplos de posibles preguntas:
#### **1.** ¿Cuántos casos de tiroteos se han registrado en los últimos años en cada estado de EE.UU., especificando el número total de muertos, heridos y víctimas en cada caso?

#### **2.** ¿Cuántos de los tiradores involucrados en tiroteos tenían antecedentes de problemas de salud mental?

#### **3.** ¿Cuántos de los tiradores adquirieron legalmente sus armas?

