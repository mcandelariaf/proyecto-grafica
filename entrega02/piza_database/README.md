El proceso de limpieza se realizó primero desde el archivo Excel original. Eliminé las paginas de intro, shooter y victim, dejando solo la página incident. Luego, en esta página eliminé todos los sucesos que ocurrieron antes de 2017, y eliminé las columnas de variables que no me eran útiles para mi objetivo. Elimine las columnas Incident ID, Sources, number news, media attention, reliability, quarter, school level, location, location type, during school, time period, first shot, narrative, situation, accomplice, hostages, barricade, officer involved, bullied, domestic violence, gang related, preplanned, shors fired y active shooter FBI.

Luego transformé el archive a csv y lo llevé a Collab.
Ahí importé los pandas y leí mi base de datos con los códigos import pandas as pd y df = pd.read_csv("/content/drive/MyDrive/datos.csv"). Luego con una serie de comandos verifiqué la correcta visualización y compatibilidad de la base de datos. Dentro de estos hay códigos como print(df.head()) o print(df.describe()).
Luego para limpiar todos los NaN usé el código df_final = df.dropna(subset=['Incident_ID'], axis=0), con cada columna. El tema es que al printear, seguían habiendo datos erróneos al no ser datos cuantitativos, sino cualitativos.

Para eso apliqué el comando df_limpio = df.dropna() print(df_limpio), para eliminar todas las casillas que contuvieran un null, pudiendo limpiar de datos erróneos la base de datos.

Después para ver la frecuencia de las ciudades, usé los comandos ciudades_frecuentes = df['City'].value_counts() print(ciudades_frecuentes) para poder visualizarlas en una tabla. Lo mismo hice pero cambiando el object de City a State. 
Al ver que en el caso de las ciudades no se imprimían todas al ser un total de 506, usé los códigos groupby para tomar las dos columnas de City y State juntas. Luego usé .sort_values(ascending=False) cosa de que las categorías se ordenaran de manera descendente el frecuencia. De ahí usé la función head para saber 50 más repetidas, debido a la gran cantidad de ciudades que solo aparecían una vez en toda la base de datos,razón por la cual no las consideré relevantes en el análisis.
Por ultimo, usé df_top_50=top_50_ciudades_estados.reset_index (name='repeticiones') print(df_top_50) para crear un dataframe indexados con repeticiones para tener una visualización más sencilla de los datos.

De base usé https://www.chds.us/sssc/data-map/  que es una base de datosque recopila todos estos incidentes en estados unidos desde 1970 a 2023, que permite tener un buen alcance histórico de los sucesos en este país.

Preguntas que se pueden responder: ¿Cuál es el estado con más tiroteos? ¿Cuál es la ciudad con más tiroteos? ¿Cuál es el año con más tiroteos?




Los datos eran tanto cualitativos como cuantitativos, pero su mayoría cualitativos. El alcancé metodológico del resultado de la limpieza es una base de datos con la que construir herramientas graficas de orientación para el usuario en el tema, como podría ser un gráfico. En el archivo csv luego de la primera limpieza quedan las categorías incident id con el cual se identifican internamente en la tabla los incidentes tabulados, la fecha en la que sucedieron, la escuela donde sucedieron, la ciudad, el estado, el sumario donde se describe la situación que ocurrió y los blancos de las balas disparadas durante el suceso. En el resultado de los códigos queda la categorías ciudad y estado y el índice repeticiones.

Era una base bastante completa, con varias perspectivas de los hechos: lugar, hora, si fueron durante tiempo de clases, con que tipo de violencia estaba relacionado (domestica, de pandillas), el alcancé de los medios en su cobertura, etc.

