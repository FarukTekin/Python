import pandas
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("polynomial.csv", sep=";")

#polynomial_regression = PolynomialFeatures(degree=2)

print(df)

plt.scatter(df["deneyim"], df["maas"])
plt.xlabel("Deneyim (Yıl)")
plt.ylabel("Maaş")
plt.show()
"""
reg = LinearRegression()
reg.fit(df[["deneyim"]], df["maas"])
plt.xlabel("Deneyim (Yıl)")
plt.ylabel("Maaş")
plt.scatter(df["deneyim"], df["maas"])
xekseni = df["deneyim"]
yekseni = reg.predict(df[["deneyim"]])
plt.plot(xekseni, yekseni, color="g", label="Lineer Regression")
plt.show()
"""
polynomial_regression = PolynomialFeatures(degree=5)
x_polynomial = polynomial_regression.fit_transform(df[["deneyim"]])
reg = LinearRegression()
reg.fit(x_polynomial, df["maas"])

y_head = reg.predict(x_polynomial)
plt.plot(df["deneyim"], y_head, color="red", label="polynomial regression")
plt.legend()
plt.scatter(df["deneyim"], df["maas"])
plt.show()

x_polynomial1 = polynomial_regression.fit_transform([[4.5]])
print(reg.predict(x_polynomial1))
