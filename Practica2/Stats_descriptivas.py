import pandas as pd
#min, max,media, moda conteo, sumatoria, varianza, desviación estandar, kurtosis
def shout_stats(df, columna):
    print(f"\n--- Estadisticas descriptivas de la columna {columna} ---")
    serie = df[columna]   # para abreviar
    print("Mínimo:", serie.min())
    print("Máximo:", serie.max())
    print("Media:", serie.mean())
    print("Moda:", serie.mode().iloc[0])  
    print("Conteo:", serie.count())      
    print("Sumatoria:", serie.sum())
    print("Varianza:", serie.var())
    print("Desviación estándar:", serie.std())
    print("Curtosis:", serie.kurt())
    return


df = pd.read_csv("../vgsales%20(1).csv")
#Estadisticas del metodo describe
print("\n--- Estadisticas automaticas ---")
print(df.describe(include="number"))
#Estadisticas descriptivas, especificas para una columna
shout_stats(df, "Global_Sales")

#
print("\n--- Estadisticas por grupo ---")
estadisticas = df.groupby("Platform")["Global_Sales"].agg(["mean", "sum", "count"])
print(estadisticas)