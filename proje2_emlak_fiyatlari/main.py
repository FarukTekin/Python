import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import pickle

df = pd.read_csv("multilinearregression.csv", sep=";")

reg = linear_model.LinearRegression()
reg.fit(df[["alan", "odasayisi", "binayasi"]], df["fiyat"])

print(reg.predict([[230, 4, 10]]))

#reg.coef_
#reg.intercept_

model_file = "ev_fiyat_tahmini_mlr_model.pickle"
pickle.dump(reg, open(model_file, "wb"))
