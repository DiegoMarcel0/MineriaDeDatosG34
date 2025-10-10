import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt


def regresion_linearM(df, x_columns, y_column):
    #1. seleccionar grupos
    y = df[y_column]        # Ventas que modelar
    X = df[x_columns]    # Ventas de las demas regiones
    # 2. Dividir en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Crear y entrenar el modelo lineal
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    # 4. Hacer predicciones
    y_pred = modelo.predict(X_test)

    # 5. Calcular el R² 
    r2 = r2_score(y_test, y_pred)# Comparado con otros datos
    r2_traint = modelo.score(X_train, y_train)# Solo del modelo
    print(f"R² del modelo: {r2:.4f}")
    print(f"R² (sin comparar) del modelo: {r2_traint:.4f}")
    # 6. Mostrar la relación real vs predicha
    plt.figure(figsize=(6,6))
    plt.scatter(y_test, y_pred, alpha=0.7)
    print("y_test: ")
    print(y_test)
    print("y_pred: ")
    print(y_pred)
    #plt.xlim(0, 1)   # límites del eje X 
    #plt.ylim(0, 1)   # límites del eje Y
    plt.xscale("log")
    plt.yscale("log")
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel("Ventas reales (log)")
    plt.ylabel("Ventas predichas (log)")
    plt.title(f"Sobre las ventas de {y_column}\nR² del modelo: {r2:.4f} ")
    plt.show()
    return 

"""
Regresión lineal multiple de las ventas de una región en base 
a las ventas de las otras regiones
"""
df = pd.read_csv("../vgsales%20(1).csv")
regresion_linearM(df, ["JP_Sales", "NA_Sales", "Other_Sales"], "EU_Sales")


"""
Resultados de prueba de EU(#2):
R² del modelo: 0.7769
Conclusion:
Probando varias combinaciones, este es de los que mejor resultados muestra,
tanto por la grafica como por el coeficiente de determinación.
Los datos si parecen tender a la recta del modelo.

Como dato adicional, primero no se uso escala logaritmica (#1), pero aunque
se limitara la escala, gran cantidad de datos tienden a valores bajos, asi que se 
eligio la escala logaritmica porque permite ver los puntos, tanto altos como bajos.
"""
regresion_linearM(df, ["EU_Sales", "NA_Sales", "Other_Sales"], "JP_Sales")
"""
Resultados de prueba de Japon(#3):
R² del modelo: 0.1176
Las ventas de Japon son de las que peor coeficiente de determinación tiene, es decir, 
es el que peor se puede explicar con las ventas de las demás regiones, me inclino a pensar que
es por una cultura independiente que tiene del resto del mundo, teniendo tendencias más
independientes

"""
regresion_linearM(df, ["NA_Sales", "Other_Sales"], "EU_Sales")

"""
Resultados de Prueba adicional Sobre EU (sin datos de Japon)
R² del modelo: 0.7799
Aunque graficamente no mejoro, parece ser que no tomar
en cuenta los datos e japon mejoro el modelo, al menos si
solo se toma en cuenta R²

"""