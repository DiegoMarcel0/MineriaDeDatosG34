from matplotlib import cm
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

#  Cargar dataset
df = pd.read_csv("../vgsales%20(1).csv")
#Japón y North America son bastante diferentes entre si, esto inferido de la practica 5
df = df[["NA_Sales", "JP_Sales"]]
#  Normalizar (es importante para que todas las variables pesen igual)
scaler = StandardScaler()
scaled = scaler.fit_transform(df)

# Metodo del codo para visualizar el mejor numero de clusters
inertia = []
K = range(1, 10)

for k in K:
    model = KMeans(n_clusters=k, random_state=0)
    model.fit(scaled)
    inertia.append(model.inertia_)
#print(inertia)
plt.plot(K, inertia, 'bo-')
plt.xlabel('Número de clusters')
plt.ylabel('Inercia')
plt.title('Método del codo')

plt.show()

"""
Se encontro de que 5 es el numero de clusteres con el que se deja de ser significativo
el la disminución de distancia a los centroides, esto solo de forma intuitiva.
"""
#  Crear el modelo de clustering
kmeans = KMeans(n_clusters=5, random_state=0)
df['Cluster'] = kmeans.fit_predict(scaled)

# *** Graficar con colores automáticos ***
# Asignar colores
num_clusters = len(df['Cluster'].unique())
colormap = cm.get_cmap('viridis', num_clusters)
colors = [colormap(i) for i in range(num_clusters)]
#Dividir y mostrar
plt.figure(figsize=(7,5))
for i in range(num_clusters):
    subset = df[df['Cluster'] == i]
    plt.scatter(subset['NA_Sales'], subset['JP_Sales'],
                color=colors[i], label=f'Cluster {i}')
plt.xlabel('NA_Sales')
plt.ylabel('JP_Sales')
plt.title('Clusters de ganancias')
plt.legend(title='Clusters', loc='upper right')
plt.show()


"""
Conclusiones
Esto puede usarse para clasificar el exito de los juegos, estableciendo
5 tipos de rendimientos, según el exito total o parcial y la región donde más gusto
Por ejemplo se puede clasificar como (según en la grafica):
Cluster 0: De exito minimo
Cluster 1: Gran exito en Japón
Cluster 2: Exito en Norte America
Cluster 3: Exito General (Mayoritariamente en Japón)
Cluster 4: Exito en Japón


NOTA: No se espera ver un patron de los datos con respecto a las clases que ya se conocen,
esto se demuestra en la practica anterior
"""