import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

url = (
    "https://raw.githubusercontent.com/lorey/list-of-countries/master/csv/countries.csv"
)

df = pd.read_csv(url, sep=";")
print(df.head(5))

print("Cantidad de Filas y columnas:", df.shape)
print("Nombre de columnas:", df.columns)
df.info()
df.describe()
corr = df.set_index("alpha_3").select_dtypes(include="number").corr()
sm.graphics.plot_corr(corr, xnames=list(corr.columns))
plt.show()

url = "https://raw.githubusercontent.com/DrueStaples/Population_Growth/master/countries.csv"
df_pop = pd.read_csv(url)
print(df_pop.head(5))
df_pop_es = df_pop[df_pop["country"] == "Spain"]
print(df_pop_es.head())
df_pop_es.drop(["country"], axis=1)["population"].plot(kind="bar")
