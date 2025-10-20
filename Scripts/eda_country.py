import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

url = 'https://raw.githubusercontent.com/lorey/list-of-countries/master/csv/countries.csv'

df = pd.read_csv(url, sep=";")
print(df.head(5))

print('Cantidad de Filas y columnas:', df.shape)
print('Nombre de columnas:', df.columns)
df.info()
df.describe()
corr = df.set_index('alpha_3').select_dtypes(include='number').corr()
sm.graphics.plot_corr(corr, xnames=list(corr.columns))
plt.show()