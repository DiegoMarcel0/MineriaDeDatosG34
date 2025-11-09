import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos
x = np.linspace(0, 10, 50)
y = 3*x + np.random.normal(0, 3, 50)

# Ajuste del modelo
modelo = LinearRegression()
modelo.fit(x.reshape(-1, 1), y)

# Predicciones
x_pred = np.linspace(0, 10, 100)
y_pred = modelo.predict(x_pred.reshape(-1, 1))

# Estimamos desviación estándar de residuos
y_hat = modelo.predict(x.reshape(-1, 1))
residuos = y - y_hat
s_err = np.sqrt(np.sum(residuos**2) / (len(x) - 2))

# Calculamos intervalo de confianza del 95%
from scipy import stats
t = stats.t.ppf(0.975, len(x)-2)
conf = t * s_err * np.sqrt(1/len(x) + (x_pred - np.mean(x))**2 / np.sum((x - np.mean(x))**2))

# Gráfica
plt.scatter(x, y, color='blue', label='Datos')
plt.plot(x_pred, y_pred, color='red', label='Regresión')
plt.fill_between(x_pred, y_pred - conf, y_pred + conf, color='red', alpha=0.2, label='Intervalo 95%')
plt.legend()
plt.show()
