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
    plt.xscale("log")
    plt.yscale("log")
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel("Ventas reales (log)")
    plt.ylabel("Ventas predichas (log)")
    plt.title(f"Sobre las ventas de {y_column}\nR² del modelo: {r2:.4f} ")
    plt.show()
    return 


df = pd.read_csv("../vgsales%20(1).csv")

regresion_linearM(df, ["JP_Sales", "NA_Sales", "Other_Sales"], "EU_Sales")
regresion_linearM(df, ["EU_Sales", "NA_Sales", "Other_Sales"], "JP_Sales")
#regresion_linearM(df, ["NA_Sales", "Other_Sales"], "EU_Sales")

##Comparación de ventas entre regiones
dummy_df = df.groupby("Year")["Other_Sales"].agg(["sum"])
dummy_df = dummy_df.reset_index()
plt.plot(dummy_df['Year'], dummy_df["sum"], label='Otros')

dummy_df = df.groupby("Year")["NA_Sales"].agg(["sum"])
dummy_df = dummy_df.reset_index()
plt.plot(dummy_df['Year'], dummy_df["sum"], label='NA')

dummy_df = df.groupby("Year")["JP_Sales"].agg(["sum"])
dummy_df = dummy_df.reset_index()
plt.plot(dummy_df['Year'], dummy_df["sum"], label='JP')

dummy_df = df.groupby("Year")["EU_Sales"].agg(["sum"])
dummy_df = dummy_df.reset_index()
plt.plot(dummy_df['Year'], dummy_df["sum"], label='EUA')

plt.xlabel('Año')
plt.ylabel('Ventas')
plt.title('Comparación de ventas por región')
plt.legend()
plt.grid(True)
plt.show()

#Comparación por genero
grouped = df.groupby("Genre")[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].sum()
grouped = grouped.sort_values(by="NA_Sales", ascending=False, inplace=False)
grouped.plot(kind="bar", figsize=(10,5))
plt.title("Ventas por género y región")
plt.ylabel("Ventas")
plt.tight_layout()
plt.show()

##Comparación de ventas entre regiones
dummy_df = df.groupby("Genre")["Other_Sales"].agg(["sum"])
dummy_df = dummy_df.reset_index()
plt.plot(dummy_df['Genre'], dummy_df["sum"], label='Otros')

dummy_df = df.groupby("Genre")["NA_Sales"].agg(["sum"])
dummy_df = dummy_df.reset_index()
plt.plot(dummy_df['Genre'], dummy_df["sum"], label='NA')

dummy_df = df.groupby("Genre")["JP_Sales"].agg(["sum"])
dummy_df = dummy_df.reset_index()
plt.plot(dummy_df['Genre'], dummy_df["sum"], label='JP')

dummy_df = df.groupby("Genre")["EU_Sales"].agg(["sum"])
dummy_df = dummy_df.reset_index()
plt.plot(dummy_df['Genre'], dummy_df["sum"], label='EU')

plt.xlabel('Genre')
plt.ylabel('Ventas')
plt.title("Ventas por género y región")
plt.legend()
plt.grid(True)
plt.show()




regions = {
    "North America": "NA_Sales",
    "Europe": "EU_Sales",
    "Japan": "JP_Sales",
    "Other Regions": "Other_Sales"
}

# Crear un subplot por región
fig, axes = plt.subplots(1, 4, figsize=(18, 5))

for ax, (region_name, col) in zip(axes, regions.items()):
    
    # Agrupar las ventas por plataforma
    platform_sales = df.groupby("Platform")[col].sum()
    
    # Ordenar y tomar las top 5 plataformas para evitar un pastel con 20 segmentos
    top5 = platform_sales.sort_values(ascending=False).head(5)
    
    ax.pie(top5, labels=top5.index, autopct='%1.1f%%')
    ax.set_title(f"Ventas por plataforma en {region_name}")

plt.tight_layout()

print((df["Name"].value_counts().reset_index())["count"].value_counts())

plt.show()


