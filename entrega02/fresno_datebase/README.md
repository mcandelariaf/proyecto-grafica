# Limpieza de datos
## Candelaria Fresno

1.	Desde el archivo excel de la base de datos bruta, eliminé las hojas: cover, shooter, victim y weapon, para quedarme con los datos principales de la hoja “incidents”.
2.	En esta hoja eliminé desde Excel todos los casos desde 2017 hacia atrás ya que nuestra hipótesis se centra en los últimos seis años. Además de las siguientes columnas: Source, Number_News, Media_Attention, Reliability, Time_Period, First_Shot, Summary, Narrative, Accomplice, Accomplice_Narrative, Hostages, Barricade, Officer_Involved, Bullied, Domestic_Violence, Gang_Related, Active_Shooter_FBI, Shots_Fired, LAT, LNG.
3.	Convertí el archivo Excel a un archivo csv y así poder trabajar los datos con Python desde Google Colab. 
4.	Desde Google Colab subí la base de datos (incidentes.csv) y la cargué como dataframe.
5.	Luego eliminé las columnas Quarter y Location_Type y descargué la base de datos limpia (incidentes_limpio.csv). 
6.	Jugué un poco con los datos y generé cuatro códigos que nos permiten responder las siguientes preguntas: 
__¿Cuáles son los estados con una mayor cantidad de incidentes armados en colegios en los últimos seis años? 
¿Cómo ha evolucionado la cantidad de tiroteos con el pasar de los años?
¿Cuántas víctimas fatales ha habido? ¿Y víctimas totales?__

Nombre de la base: Public v3.1 K-12 School Shooting Database (3 29 2024)
[Fuente](https://k12ssdb.org/)  
