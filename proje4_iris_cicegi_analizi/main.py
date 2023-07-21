import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

url = "pca_iris.data"

df = pd.read_csv(url, names= ["sepal length", "sepal width", "petal length", "petal width", "target"])

#print(df)

features = ["sepal length", "sepal width", "petal length", "petal width"]
x = df[features]
y = df["target"]

x = StandardScaler().fit_transform(x)
#print(x)

pca = PCA(n_components=2)
principalCompenents = pca.fit_transform(x)
principalDf = pd.DataFrame(data=principalCompenents, columns=["principal component 1", "principal component 2"])
#print(principalDf)

final_dataframe = pd.concat([principalDf, df[["target"]]], axis=1)
#print(final_dataframe.head())
"""
dfSetosa = final_dataframe[df.target == "Iris-setosa"]
dfVirginica = final_dataframe[df.target == "Iris-virginica"]
dfVersicolor = final_dataframe[df.target == "Iris-versicolor"]
plt.xlabel("principal component 1")
plt.ylabel("principal component 2")
plt.scatter(dfSetosa["principal component 1"], dfSetosa["principal component 2"], color="green")
plt.scatter(dfVirginica["principal component 1"], dfVirginica["principal component 2"], color="red")
plt.scatter(dfVersicolor["principal component 1"], dfVersicolor["principal component 2"], color="blue")
plt.show()
"""
targets = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
colors = ["g", "b", "r"]
plt.xlabel("principal component 1")
plt.ylabel("principal component 2")

for target, col in zip(targets, colors):
    dftemp = final_dataframe[df.target == target]
    plt.scatter(dftemp["principal component 1"], dftemp["principal component 2"], color=col)
plt.show()

print(pca.explained_variance_ratio_)
print(pca.explained_variance_ratio_.sum())
