# -*- coding: utf-8 -*-
"""encargo02

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YBLqdFZG2a-Kjpc37JiCfuNOfj03IxOs
"""

import pandas as pd

# Cargar la base de datos
tiroteos = pd.read_csv("tiroteos.csv")

# Visualizar las primeras filas para entender la estructura de los datos
print(tiroteos.head())

# Filtrar las columnas necesarias
tiroteos_limpios = tiroteos[["case", "location", "fatalities", "injured", "total_victims",
                              "age_of_shooter", "gender", "prior_signs_mental_health_issues", "mental_health_details", "weapons_obtained_legally","year"]]

# Filtrar los datos desde el año 2017 en adelante
tiroteos_limpios = tiroteos_limpios[tiroteos_limpios["year"] >= 2017]

# Visualizar las primeras filas de la base de datos limpia
print(tiroteos_limpios.head())

# Guardar la base de datos limpia en un nuevo archivo CSV
tiroteos_limpios.to_csv("tiroteos_limpios.csv", index=False)