import pandas as pd

df = pd.read_csv("outlier_ornek_veriseti.csv", sep=";")
print(df)
print(df.describe())
Q1 = df.boy.quantile(0.25)
Q3 = df.boy.quantile(0.75)
print(Q1, Q3)

IQR_degeri = Q3 - Q1
print(IQR_degeri)

alt_limit = Q1 - 1.5*IQR_degeri
ust_limit = Q3 + 1.5*IQR_degeri
print(alt_limit, ust_limit)

aykiri_degerler = df[(df.boy < alt_limit) | (df.boy > ust_limit)]
print(aykiri_degerler)

df_filtrelenmis = df[(df.boy > alt_limit) & (df.boy < ust_limit)]
print(df_filtrelenmis)
