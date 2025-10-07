import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
"""
Regresión lineal de las ventas de una región en base 
a las ventas de las otras regiones
"""
# 1. Leer el CSV y seleccionar grupos
df = pd.read_csv("../vgsales%20(1).csv")
y = df["JP_Sales"]                      # Región que quieres predecir
X = df[["EU_Sales", "NA_Sales", "Other_Sales"]]    # Las demás regiones son las variables predictoras

# 3. Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Crear y entrenar el modelo lineal
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 5. Hacer predicciones
y_pred = modelo.predict(X_test)

# 6. Calcular el R² (qué tan bien explica las ventas)
r2 = r2_score(y_test, y_pred)
print(f"R² del modelo: {r2:.4f}")

# 7. Mostrar la relación real vs predicha
plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.xscale("log")
plt.yscale("log")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel("Ventas reales (log)")
plt.ylabel("Ventas predichas (log)")
plt.title("Ventas reales vs predichas (escala logarítmica)\nPredicción de las ventas de EU")
plt.show()
"""
Resultados de prueba #1:
R² del modelo: 0.7769
Conclusion:
Probando varias combinaciones, este es de los que mejor resultados muestra,
tanto graficamente como en el coeficiente de determinación.
Se puede argumentar que los datos estan muy correlacionados, al estar hablando de un mismo producto,
el cual tiene exito dependiendo de si es bueno o no, y las ventas solo se ajustan a la economia local.

Como dato adicional, las ventas de Japon son las que peor coeficiente de determinación tiene,
Es el que peor se puede explicar con las ventas de las demás regiones, me inclino a pensar que
es por la cultura tan independiente que tiene del resto del mundo, teniendo tendencias más
independientes

 """

