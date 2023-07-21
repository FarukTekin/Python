import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import pickle

myModel = pickle.load(open("ev_fiyat_tahmini_mlr_model.pickle", "rb"))

print(myModel.predict([[230, 4, 10]]))
