import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

def regresion_linearS(df, x_column, y_column):
    #1. seleccionar grupos
    y = df[y_column]        # Escala de tiempo de ventas  
    X = df[[x_column]]    # Ventas anuales}
    # 2. Dividir en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Crear y entrenar el modelo lineal
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    # 4. Hacer predicciones
    y_pred = modelo.predict(X_test)

    # 5. Calcular el R² (qué tan bien explica las ventas)
    r2 = r2_score(y_test, y_pred)
    print(f"R² del modelo: {r2:.4f}")
    # 6. Mostrar la relación real vs predicha
    plt.scatter(X, y, label="Datos reales")
    plt.plot(X, modelo.predict(X), color='red', label="Recta de regresión")
    plt.xlabel(f"{x_column}")
    plt.ylabel(f"{y_column}")
    plt.title(f"Regresión Linear simple\nR² del modelo: {r2:.4f} ")
    plt.legend()
    plt.show()
    return 

def graficare(df, region):
    promedio_anual = df.groupby("Year")[region].agg("mean")
    promedio_anual = promedio_anual.reset_index()
    #print(promedio_anual)
    regresion_linearS(promedio_anual, "Year", region)
"""
Regresión lineal de las ventas (global o regional) a lo largo del tiempo
Los datos estan agrupados por AÑO y se saco el promedio
NOTA: No se obtienen buenos resultados si no se agrupa
"""
df = pd.read_csv("../vgsales%20(1).csv")
df = df.dropna(subset=["Year"]) #Eliminar valores NA
#TEST#2
graficare(df, "EU_Sales")
#TEST#3
graficare(df, "Global_Sales")
#TEST#4
graficare(df, "JP_Sales")
"""
Resultados de prueba #2-4:
Conclusion:
Las regresiones dentro de las distintas regiones no parecen tener una relación lineal
conforme el paso del timepo, en algunos es evidente(EU_Sales Prueba#2), 
aunque en otros los resultados en cierta epoca o lapso de tiempo se comporta de forma lineal,
pero aun es facil ver los lapsos donde esto no pasa

 """

