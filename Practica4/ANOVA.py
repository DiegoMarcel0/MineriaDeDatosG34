import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro
from scipy.stats import kruskal

def barPlot(df, column1, column2, title):
    df.plot(x=column1, y=column2, kind="bar", color="purple", edgecolor="white", title=title)
    plt.tight_layout()
    plt.show()

dummy_df=pd.DataFrame()

vgsales = pd.read_csv("../vgsales%20(1).csv")

##Comprobando normalidad
publisherStats = vgsales
publisherStats["Global_Sales"] = publisherStats["Global_Sales"].round(1)
publisherStats = publisherStats.groupby("Publisher", )["Global_Sales"].value_counts()
publisherStats = publisherStats.reset_index()
#
Publisher_name = "Microsoft Game Studios"
onePublisherRoundStat = publisherStats[publisherStats["Publisher"]==Publisher_name]
onePublisherRoundStat = onePublisherRoundStat.sort_values(by="Global_Sales", ascending=True)
#print(publisherStats)
#print(onePublisherRoundStat)
barPlot(onePublisherRoundStat, "Global_Sales", "count", "¿Qué tan bien vendieron los juegos de un Publisher?")
#
Publisher_name = "NewKidCo"
onePublisherRoundStat = publisherStats[publisherStats["Publisher"]==Publisher_name]
onePublisherRoundStat = onePublisherRoundStat.sort_values(by="Global_Sales", ascending=True)
barPlot(onePublisherRoundStat, "Global_Sales", "count", "¿Qué tan bien vendieron los juegos de un Publisher?")
## Asi se ven la mayoria de las graficas de frecuencia de Global sales,
#       donde solo una minoria vende mucho y la mayoria tiene pocas ventas en comparación
# Se puede intuir que no tienen una distribución normal

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

#En ambos casos el P-value indica que hay diferencias significativas entre sus respectivos 3 grupos
#Podemos denotar que al incluir a nintendo, dichas diferencias se disparan




#NOTA: Las medidas son en millones de dolares -> .01 => 10,000 $
