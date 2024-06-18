# Visualización atómica
#### Agustín Piza

## Selección de datos
Para la visualización de datos sobre incidentes, se utilizó un archivo CSV titulado resumen_incidentes.csv. Este archivo contiene información recopilada sobre incidentes registrados a lo largo de varios años, con detalles sobre el número de incidentes, víctimas fatales y víctimas heridas por año. La selección de datos implicó inicialmente la limpieza y procesamiento de los datos originales para asegurar la coherencia y la integridad de los mismos.

## Proceso de Visualización
La visualización se realizó utilizando la biblioteca seaborn en Python, la cual facilita la creación de gráficos estadísticos claros y efectivos. Se optó por representar los datos a través de un gráfico de líneas que muestra la evolución a lo largo de los años de los incidentes, las víctimas fatales y las víctimas heridas. Esto proporciona una representación visual intuitiva de cómo estas variables han fluctuado a lo largo del tiempo.

## Ejemplos de Preguntas que Puede Responder la Visualización
1. ¿Cuál fue la tendencia general de incidentes registrados a lo largo de los años?
2. ¿Hubo algún año particularmente notable en términos de víctimas fatales o heridas?
3. ¿Existe alguna correlación entre el número de incidentes y el número de víctimas fatales o heridas?
Estas preguntas y otras similares pueden ser respondidas de manera efectiva mediante la visualización proporcionada, permitiendo una comprensión más profunda de los datos relacionados con incidentes.

## Ficha Técnica
Variables Incorporadas
* year: Año en el que ocurrieron los incidentes.
* incidents: Número total de incidentes registrados en cada año.
* total_victims_killed: Total de víctimas fatales registradas en cada año.
* total_victims_wounded: Total de víctimas heridas registradas en cada año.