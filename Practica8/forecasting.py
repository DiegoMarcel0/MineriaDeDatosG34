import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from scipy import stats

def intervalo_confianza(modelo, y, X, X_nuevos, alpha=0.05):
    """
    Calcula el intervalo de confianza para predicciones de una regresión lineal sklearn.
    """
    # Predicciones del modelo
    #y_pred = modelo.predict(X)
    y_nuevos = modelo.predict(X_nuevos)
    n = len(X)
    p = X.shape[1]  # número de variables
    gl = n - p - 1  # grados de libertad

    # Error estándar de los residuos
    s_e = np.sqrt(np.sum((y - modelo.predict(X))**2) / gl)

    # Estadístico t para el nivel de confianza
    t_val = stats.t.ppf(1 - alpha/2, gl)

    # Calcular matrices para la fórmula del error estándar de predicción
    X_mean = np.mean(X)
    Sxx = np.sum((X - X_mean)**2)

    # Error estándar de la media predicha
    SE = s_e * np.sqrt(1/n + (X_nuevos - X_mean)**2 / Sxx)
    #print("SE ->>>", s_e)
    # Intervalos inferior y superior
    lower = y_nuevos - t_val * SE.flatten()
    upper = y_nuevos + t_val * SE.flatten()

    return y_nuevos, lower, upper

def regresion_linearS(df, x_column, y_column):
    """
    Calcula y muestra los resultados de una regresión lineal simple
    
    Parámetros
    ----------
    df : pandas.dataframe
        Dataframe de los datos
    x_column : string
        nombre de la columna de la variable independiente (x)
    y_column : string
        nombre de la columna de la variable dependiente (y)
    """
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
    x = X.values

    # 6. Calcular area del intervalo de confianza
    predicciones_, low_bar_, high_bar_ = intervalo_confianza(modelo, y.values ,x , x)

    #7. Preddicciones
    ultimo_anio = df[x_column].max()
    anios_futuros = np.arange(ultimo_anio + 1, ultimo_anio + 11).reshape(-1, 1)
    predicciones, low_bar, high_bar = intervalo_confianza(modelo,y.values ,x , anios_futuros)

    #8. Mostrar datos, recta y el area de intervalo
    plt.scatter(X, y, label="Datos")#DATOS

    plt.plot(X, modelo.predict(X), color='red', label="Recta de regresión")#REGRESION
    plt.fill_between(x.flatten(), low_bar_ , high_bar_, color='red', alpha=0.2, label='Intervalo 95%')

    plt.fill_between(anios_futuros.flatten(), low_bar.flatten(), high_bar.flatten(),#PREDICCION
                    color='green', alpha=0.2, label='Intervalo 95%')
    plt.plot(anios_futuros, predicciones, color='green', linestyle='--', label='Predicción 10 años')

    plt.xlabel(f"{x_column}")
    plt.ylabel(f"{y_column}")
    plt.title(f"Regresión Linear simple + Predicciòn\nR² del modelo: {r2:.4f} ")
    plt.legend()
    plt.show()
    return 

def graficare(df, region):
    promedio_anual = df.groupby("Year")[region].agg("mean")
    promedio_anual = promedio_anual.reset_index()
    #print(promedio_anual)
    regresion_linearS(promedio_anual, "Year", region)

df = pd.read_csv("../vgsales%20(1).csv")
df = df.dropna(subset=["Year"]) #Eliminar valores NA

graficare(df, "EU_Sales")

