import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import kruskal
from scipy.stats import shapiro
#NOTA: Las medidas son en millones de dolares -> .01 => 10,000$
def barPlot(df, column1, column2, title):
    df.plot(x=column1, y=column2, kind="bar", color="purple", edgecolor="white", title=title)
    plt.tight_layout()
    plt.show()
"""
ventas_Publisher
Entrada: publisherStats->df, publisher ->String
Genera una grafica de barras del numero de juegos de un publisher
agrupados por cuanto dinero generaron.
"""
def ventas_publisher(publisherStats, publisher):
    publisherStats["Global_Sales"] = publisherStats["Global_Sales"].round(1)
    publisherStats = publisherStats.groupby("Publisher", )["Global_Sales"].value_counts()
    publisherStats = publisherStats.reset_index()
    onePublisherRoundStat = publisherStats[publisherStats["Publisher"]==publisher]
    onePublisherRoundStat = onePublisherRoundStat.sort_values(by="Global_Sales", ascending=True)
    stat, p = shapiro(onePublisherRoundStat["Global_Sales"])
    title = f"Ventas de {publisher} \n  -> W-stat:{stat} |p-value: {p:.2f}"
    barPlot(onePublisherRoundStat, "Global_Sales", "count", title)
    return 


#Leer csv
vgsales = pd.read_csv("../vgsales%20(1).csv")
"""
Para estudiar la normalidad de las graficas, se graficaran, de cierto publisher
el numero de juegos según que tanto dinero genero
"""
ventas_publisher(vgsales, "Microsoft Game Studios")
#
ventas_publisher(vgsales, "Nintendo")
"""
Graficas de Microsoft Game Studio y Nintendo
Conclusión:
Se puede intuir que no tienen una distribución normal o que tal vez no se encuentran los
datos de los videojugos que perdieron dinero para formar la cola izquierda de la grafica normal
En todo caso la prueba de Shapiro-Wilk muestra que estos datos no se comportan según
la distribución normal
"""

#Prueba de Normalidad Shapiro-Wilk sobre el resto de Publishers
game_2 = 0
no_normal = 0
ye_normal = 0
for publisher in vgsales["Publisher"].unique():
    games_in_publisher = vgsales[vgsales["Publisher"]==publisher].shape[0]
    if games_in_publisher <= 3:
        game_2 = game_2 + 1
    else: 
        stat, p = shapiro(vgsales.loc[vgsales["Publisher"]==publisher, "Global_Sales"])
        if p >= 0.5:
            print(f"Publisher {publisher} -> W-stat:{stat} |p-value: {p:.4f}")
            ye_normal = ye_normal + 1
            #Verificación de graficas, son bastantes parece POP UPS de spam de antes
            #ventas_publisher(vgsales, publisher)
        else:
            no_normal = no_normal+1
print(f"Publishers sin datos suficientes: {game_2}")
print(f"Publisher, cuyas ventas no siguen la normal: {no_normal}")
print(f"Publisher, cuyas ventas si siguen la normal: {ye_normal}")
"""
Resultasdos:
Publishers sin datos suficientes: 315
Publisher, cuyas ventas no siguen la normal: 244
Publisher, cuyas ventas si siguen la normal: 20

Conclusión:
Despues de analizar las graficas donde se tienen casos como la de RedOctane,
donde los datos no parecen, pero la prueba arroja que si es Normal, una gran parte no tiene
suficiente variabilidad, tienen todas sus ventas (3-20) en un solo campo (0.0, 0.1, 0.2...)
Además, son una minoria(20/264).
Por estas razones, para trabajar con los datos no se asumira normalidad.
"""

#Prueba no parametrica de Kruskal-Wallis, para sustituir la prueba ANOVA regular
publisherA = "Microsoft Game Studios"
publisherB = "Activision"
publisherC = "Sony Computer Entertainment"
gA = vgsales[vgsales["Publisher"]==publisherA]["Global_Sales"]
gB = vgsales[vgsales["Publisher"]==publisherB]["Global_Sales"]
gC = vgsales[vgsales["Publisher"]==publisherC]["Global_Sales"]
h_stat, p_val = kruskal(gA, gB, gC)
print("Prueba con Microsoft Game Studios, Activision y Sony Computer Entertainment")
print("Kruskal-Wallis -> H:", h_stat, "p-value:", p_val)


publisherA = "Microsoft Game Studios"
publisherB = "Activision"
publisherC = "Nintendo"
gA = vgsales[vgsales["Publisher"]==publisherA]["Global_Sales"]
gB = vgsales[vgsales["Publisher"]==publisherB]["Global_Sales"]
gC = vgsales[vgsales["Publisher"]==publisherC]["Global_Sales"]
h_stat, p_val = kruskal(gA, gB, gC)
print("Prueba con Microsoft Game Studios, Activision y Nintendo")
print("Kruskal-Wallis -> H:", h_stat, "p-value:", p_val)

""" 
#En ambos casos el P-value indica que hay diferencias significativas entre sus respectivos 3 grupos
#Podemos denotar que al incluir a nintendo, dichas diferencias se disparan
 """




