import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

#Outcome = 1 --> Diabetes
#Outcome = 0 --> No Diabetes

data = pd.read_csv("diabetes.csv")
#print(data.head())

"""
diabetes = data[data.Outcome == 1]
no_diabetes = data[data.Outcome == 0]

plt.scatter(no_diabetes.Age, no_diabetes.Glucose, color="green", label="No Diabetes", alpha=0.5)
plt.scatter(diabetes.Age, diabetes.Glucose, color="red", label="Diabetes", alpha=0.5)
plt.xlabel("Age")
plt.ylabel("Glucose")
plt.legend()
plt.show()
"""
y = data.Outcome.values
x_raw_data = data.drop(["Outcome"], axis=1)

x = (x_raw_data - np.min(x_raw_data)) / (np.max(x_raw_data) - np.min(x_raw_data))
#print("Raw data before normalization\n", x_raw_data.head())
#print("Raw data after normalization\n", x.head())

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

count = 1
for k in range(1, 11):
    new_knn = KNeighborsClassifier(n_neighbors=k)
    new_knn.fit(x_train, y_train)
    print(count, " ", "accuracy rate", new_knn.score(x_test, y_test)*100)
    count += 1

#For New Predict
sc = MinMaxScaler()
sc.fit_transform(x_raw_data)
new_prediction = new_knn.predict(sc.transform(np.array([[6, 148, 72, 35, 0, 33.6, 0.627, 50]])))
print(new_prediction[0])
