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

#Verificar tipo de cada columna por que son muchos, para que no se cuele un dato raro
validar_tipos("vgsales%20(1).csv", tipos)
""" SALIDA:
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
df = pd.read_csv("vgsales%20(1).csv")
valores_invalidos = df[~df["Year"].between(1900, 2100, inclusive="both")]
print(f"\n--- Validación de la columna Year ---")
if valores_invalidos.empty:
    print(f"-> Todos los valores están entre 1900 y 2100.")
else:
    print(f"X Se encontraron valores fuera de rango :")
    print(valores_invalidos[["Year"]])

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

#Por situaciones similares en los videos de la clase, se opto por:
#   Dejar el .cvs tal cual, pero en calculos donde se incluya "Year" eliminar los NaN

#Ejemplo de convertir y limpiar NaN
df = pd.read_csv("vgsales%20(1).csv")
df = df.dropna(subset=["Year"])
df["Year"] = df["Year"].astype("int64")
#df.to_csv("vgsales_NoNA.csv", index=False)
print("\n--- Finalizado---\n\n")
"""
--- Finalizado---

"""
#Comprobacion
#TIPO
print(f"\n--- Validación de la columna Year ---")
tipo_real = str(df["Year"].dtype)

if tipo_real == "int64":
    print("-> 'Year': int64 (correcto)")
else:
    print(f"X 'Year': {tipo_real} (se esperaba int64)")

#Sin algún NaN
valores_invalidos = df[~df["Year"].between(1900, 2100, inclusive="both")]
if valores_invalidos.empty:
    print(f"-> Todos los valores están entre 1900 y 2100.")
else:
    print(f"X Se encontraron valores fuera de rango :")
    print(valores_invalidos[["Year"]])
"""
--- Validación de la columna Year ---
-> 'Year': int64 (correcto)
-> Todos los valores están entre 1900 y 2100.
"""
#Todo OK