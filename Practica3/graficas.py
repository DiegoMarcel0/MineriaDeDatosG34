import pandas as pd
import matplotlib.pyplot as plt

def linePlot(df, column1, column2, title):
    df.plot(x=column1, y=column2, kind="line", marker="o", color="b", title=title)
    #plt.plot(df[column1], df[column2])
    #df.plot(x=x, y=y, kind="line", marker="o", title=f"Línea: {y} vs {x}")
    plt.show()

def scatterPlot(df, column1, column2, title):
    #df.scatter(x=column1, y=column2, color="r", title=title)
    plt.scatter(df[column1], df[column2], color="r")
    plt.show()

def barPlot(df, column1, column2, title):
    df.plot(x=column1, y=column2, kind="bar", color="purple", edgecolor="white", title=title)
    plt.tight_layout()
    plt.show()

def PiePlot(df , column1, column2, title):
    #df.plot(x=column1, y=column2, kind="pie", startangle=90)
    plt.pie(df[column1], labels=df[column2], autopct="%1.1f%%")
    plt.title(title)
    plt.show()

def histPlot(df, column1, title):
    plt.figure(figsize=(12, 5))
    #plt.hist(df[column1], bins=12, color="orange", edgecolor="black")
    plt.hist(df[column1])
    plt.title(title)
    plt.xlabel(column1)
    plt.ylabel("Frecuencia")
    #plt.tight_layout()
    plt.show()
"""
column1 -> En que queremos categorizar los datos
column2 -> datos
"""
def boxplotPlot(df , column1, column2, title):
    #plt.boxplot([grupo1, grupo2, grupo3], labels=["Grupo 1", "Grupo 2", "Grupo 3"])
    grupos = []
    categoriaLista =[]
    categoriaSerie = df.groupby(column1)[column2].count()
    categoriaSerie = categoriaSerie.reset_index()
    for categoria in categoriaSerie[column1]:
        dummyDF= df[df[column1]==categoria][column2]
        dummyDF = dummyDF.reset_index()
        #print(dummyDF.count())
        #print(dummyDF[column2])
        if (dummyDF.count()[column2]>1000):
            grupos.append(dummyDF[column2])
            categoriaLista.append(categoria)
        
    #print(grupos)
    #print(categoriaLista)
    plt.boxplot(grupos, tick_labels=categoriaLista,
                patch_artist=True,  # activa relleno de color
                boxprops=dict(facecolor="skyblue", color="black"),
                medianprops=dict(color="red", linewidth=2),
                whiskerprops=dict(color="black", linewidth=1),
                capprops=dict(color="black", linewidth=1),
                flierprops=dict(marker="o", markersize=5, markerfacecolor="orange")
                )
    plt.title(title)
    plt.ylabel(column1)
    plt.grid(axis="y", linestyle="--", alpha=0)
    plt.show()


dummy_df=pd.DataFrame()

vgsales = pd.read_csv("../vgsales%20(1).csv")

publisherStats = vgsales.groupby("Publisher")["Global_Sales"].agg(["mean", "max", "count"])
publisherStats = publisherStats.reset_index()

#---------Grafica #1
#Solo las estadisticas del publisher Nintendo
dummy_df = vgsales.dropna(subset=["Year"])
dummy_df = dummy_df.sort_values(by="Year", ascending=True)
NintendoStats = dummy_df[dummy_df["Publisher"]=="Nintendo"]
NintendoStats_perYear = NintendoStats.groupby("Year")["Global_Sales"].agg(["sum"])
NintendoStats_perYear = NintendoStats_perYear.reset_index()
#Grafica de las ventas de nintendo por año
linePlot(NintendoStats_perYear, "Year", "sum", "Ventas por año de nintendo")

#---------Grafica #2
genreStats = vgsales.groupby("Genre")["Global_Sales"].agg(["mean", "max", "count"])
genreStats = genreStats.reset_index()
#print(f"Grafica de pupularidad de generos en los años {vgsales["Year"].min()} y {vgsales["Year"].max()}")
barPlot(genreStats, "Genre", "count", f"Grafica de pupularidad de generos en los años {vgsales["Year"].min()} y {vgsales["Year"].max()}")

#---------Grafica #3
NintendoStats_perGenre = NintendoStats.groupby("Genre")["Global_Sales"].count()
NintendoStats_perGenre = NintendoStats_perGenre.reset_index()
#print(NintendoStats_perGenre)
PiePlot(NintendoStats_perGenre, "Global_Sales", "Genre", "Que generos preferia hacer Nintendo")

#---------Grafica #4
#Cantidad de juegos ordenada en años
histPlot(vgsales, "Year", "Histograma de cantidad de juegos")

#---------Grafica #5
#La distribucion de ganancias por año, aunque admito que no es la mejor manera de representarlo
scatterPlot(vgsales, "Year", "Global_Sales", "ola que hace")

#---------Grafica #6

boxplotPlot(vgsales , "Year", "Global_Sales", "ola")


#**************************************************** Pruebas y notas de que se hace
#fig, axs = plt.subplots(2, 2, figsize=(12, 8))
#print(publisherStats.sort_values(by="max", ascending=False))
#print(genreStats)
#linePlot(publisherStats.sort_values(by="max", ascending=False).head(20), "Publisher", "mean", "ola que hace")
#linePlot(genreStats.tail(7), "Genre", "count", "ola que hace")
#scatterPlot(genreStats.tail(7), "Genre", "mean", "ola que hace")
#barPlot(genreStats.tail(10), "Genre", "count", "ola que hace")
#PiePlot(genreStats.tail(10), "Genre", "mean", "ola que hace")
#histPlot(vgsales, "Genre", "Histograma de generos")
#**************************************************** Pruebas y notas de que se hace



