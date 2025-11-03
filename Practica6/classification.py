from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Transforma las clases a integrales y se asignan los colores
"""
Entrada: Un dataframe base
        string de la columna con las clases
Salida: Serie (convertida a int)
        Diccionario del valor (int) y su color (string) 
"""
def estandarizacion (df, y_column):
    y_original = df[y_column]
    y = y_original.astype('category').cat.codes
    #print(dict(enumerate(y_original.astype('category').cat.categories)))
    clases = df[y_column].unique()
    #print(clases)
    print("\n***Clase y su numero***")
    clases_dict = dict(enumerate(y_original.astype('category').cat.categories))
    for clave, clase in clases_dict.items():
        print(clase, " --> ", clave)
    colormap = plt.cm.get_cmap('tab10', len(clases))
    color_dict = {clase: colormap(i) for i, clase in enumerate(clases)}
    c = df[y_column].map(color_dict)
    return y, c

#Crea modelo, su score y una grafica de los datos y fronteras
"""
Entrada: Un dataframe base
        string de la columna de caracteristicas 1
        string de la columna de caracteristicas 2
        string de la columna con las clases
        numero de vecinos para el modelo de k vecinos
Salida: Serie (convertida a int)
        Diccionario del valor (int) y su color (string) 
"""
def classification_KNN(df, x_column1, x_column2, y_column, k):
    #NOTA:dos datos para una grafica más intuitiva
    X = df[[x_column1, x_column2]]
    y, c = estandarizacion(df, y_column)
    # Dividir en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    # Crear el modelo con k, usando la metrica euclidiana por defecto
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    #Medirlo con función
    y_pred = knn.predict(X_test)
    print("Precisión:", accuracy_score(y_test, y_pred))
    #PROCESO DE IMPRESIÓN DE RESULTADOS
    ## NOTA: (x,y) de coordenadas para ver donde empieza y terminan las fronteras
    x_min, x_max = X[x_column1].min() - 1, X[x_column1].max() + 1
    y_min, y_max = X[x_column2].min() - 1, X[x_column2].max() + 1
    #print (x_min ,"|||||" , x_max)
    #print (y_min ,"|||||" , y_max)
    #Crear cuadricula de 40,000 puntos (200*200)
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                        np.linspace(y_min, y_max, 200))
    #print(xx, "\n|||||||\n", yy)
    # Predecir para cada punto de la malla
    Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    #print(Z)
    #Graficar fronteras
    plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.Set1)
    #Graficar datos
    plt.scatter(df[x_column1], df[x_column2],c=c)
    plt.xlabel(x_column1)
    plt.ylabel(x_column2)
    title ="Clasificación con k-NN ("+x_column1+", "+x_column2+")"
    plt.title(title)
    #plt.legend()
    plt.xscale("log")
    plt.yscale("log")
    plt.show()

# Cargar dataset
df = pd.read_csv("../vgsales%20(1).csv")
classification_KNN(df, "EU_Sales", "NA_Sales", "Genre", 4)

onePlattform = df[df["Platform"]=="Wii"]
#print(onePlattform["Year"])
classification_KNN(onePlattform, "EU_Sales", "NA_Sales", "Genre", 5)

oneYear = df[df["Year"]==2008]
#print(oneYear)
classification_KNN(oneYear, "EU_Sales", "NA_Sales", "Genre", 3)

"""
Todos los resultados son desde confusos a intelegibles, además no parece predecir el
comportamiento de los datos, esto basandome en la función y la intuición al ver el grafico
score de 0 a 0.2 aprox

"""
df_resumen = df.groupby("Genre")[["EU_Sales", "NA_Sales"]].agg(["mean", "sum"])
df_resumen.columns = ['_'.join(col) for col in df_resumen.columns]
df_resumen = df_resumen.reset_index()
#print (df_resumen.head(5))
classification_KNN(df_resumen, "EU_Sales_mean", "NA_Sales_mean", "Genre", 3)
"""
Ya no es confuso ni intelegible, se puede ver claramente como es que no predice nada
score de 0.0
NOTA: El ejemplo viene de esta parte
"""

df_resumen = df.groupby(["Year", "Genre"])[["EU_Sales", "NA_Sales"]].agg(["mean", "sum"])
df_resumen.columns = ['_'.join(col) for col in df_resumen.columns]
df_resumen = df_resumen.reset_index()
#print (df_resumen.head(5))
classification_KNN(df_resumen, "EU_Sales_sum", "NA_Sales_sum", "Genre", 3)

"""
Resultados similares a los primeros acercamientos, confusos y no muy prometedores
score de 0 a 0.2 aprox

Conclusiones
Los datos siguen una tendencia lineal positiva, conveniente para una regresión lineal pero
no tanto para modelarlo por cercanias.
"""