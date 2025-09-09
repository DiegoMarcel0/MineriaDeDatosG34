import pandas as pd
#Valida que las columnas de un dataset tengan el tipo esperado.
def validar_tipos(ruta_csv, tipos_esperados):
    #Cargar dataset
    df = pd.read_csv(ruta_csv)
    print("\n--- Revisión de tipos de datos ---")
    for columna, tipo_esperado in tipos_esperados.items():
        if columna not in df.columns:
            print(f" La columna '{columna}' no existe en el dataset.")
            continue
        #Sacar el tipo real
        tipo_real = str(df[columna].dtype)

        if tipo_real == tipo_esperado:
            print(f"-> {columna}: {tipo_real} (correcto)")
        else:
            print(f"X {columna}: {tipo_real} (se esperaba {tipo_esperado})")

    return
#Revisa que la columna de años tenga solo valores válidos dentro de un rango.
def validar_columna_anio(ruta_csv, columna, anio_min=1900, anio_max=2100):
    #Cargar dataset
    df = pd.read_csv(ruta_csv)

    if columna not in df.columns:
        print(f"La columna '{columna}' no existe en el dataset.")
        return None

    #Detectar valores inválidos
    valores_invalidos = df[~df[columna].between(anio_min, anio_max, inclusive="both")]

    print(f"\n--- Validación de la columna '{columna}' ---")
    if valores_invalidos.empty:
        print(f"-> Todos los valores están entre {anio_min} y {anio_max}.")
    else:
        print(f"X Se encontraron valores fuera de rango en '{columna}':")
        print(valores_invalidos[[columna]])

    return 



tipos = {
    "Rank": "int64",
    "Name": "object",
    "Platform": "object",
    "Year": "int64",
    "Genre": "object",
    "Publisher": "object",
    "NA_Sales": "float64",
    "EU_Sales": "float64",
    "JP_Sales": "float64",
    "Other_Sales": "float64",
    "Global_Sales": "float64"
}

#Verificar tipo de cada columna
validar_tipos("vgsales%20(1).csv", tipos)
"""
--- Revisión de tipos de datos ---
-> Rank: int64 (correcto)
-> Name: object (correcto)
-> Platform: object (correcto)
X Year: float64 (se esperaba int64)
-> Genre: object (correcto)
-> Publisher: object (correcto)
-> NA_Sales: float64 (correcto)
-> EU_Sales: float64 (correcto)
-> JP_Sales: float64 (correcto)
-> Other_Sales: float64 (correcto)
-> Global_Sales: float64 (correcto)
"""
#CONCLUSIONES
#La salida en su mayoria esperada, queria revisar principalmente las columnas de SALES
#La unica expeción inesperada fue el año, que dio float64

# Comprobar lo de la columna Year
validar_columna_anio("vgsales%20(1).csv", columna="Year", anio_min=1900, anio_max=2100)
"""
--- Validación de la columna 'Year' ---
X Se encontraron valores fuera de rango en 'Year':
       Year
179     NaN
377     NaN
431     NaN
470     NaN
607     NaN
...     ...
16307   NaN
16327   NaN
16366   NaN
16427   NaN
16493   NaN

[271 rows x 1 columns]
"""
#CONCLUSIONES
#Se encontro que varias filas tienen NaN, por eso se reconocio como float64

#Se reemplazara con la moda de de la columna 'Year' porque
#las filas no tienen secuencia
df = pd.read_csv("vgsales%20(1).csv")
moda = df["Year"].mode()[0]
print(f"-> Moda: {moda}")
#Remplazar NA con moda
df["Year"] = df["Year"].fillna(moda)
#Corregir que sean considerado float64
df["Year"] = df["Year"].astype("int64")
df.to_csv("vgsales_NoNA.csv", index=False)
print("Finalizado")
"""
-> Moda: 2009.0
Finalizado

"""
#Comprobacion
validar_tipos("vgsales_NoNA.csv", tipos)
validar_columna_anio("vgsales_NoNA.csv", columna="Year", anio_min=1900, anio_max=2100)
"""
--- Revisión de tipos de datos ---
-> Rank: int64 (correcto)
-> Name: object (correcto)
-> Platform: object (correcto)
-> Year: int64 (correcto)
-> Genre: object (correcto)
-> Publisher: object (correcto)
-> NA_Sales: float64 (correcto)
-> EU_Sales: float64 (correcto)
-> JP_Sales: float64 (correcto)
-> Other_Sales: float64 (correcto)
-> Global_Sales: float64 (correcto)

--- Validación de la columna 'Year' ---
-> Todos los valores están entre 1900 y 2100.
"""
#Todo OK