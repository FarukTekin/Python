import pandas as pd

df = pd.read_csv("imdb_top_1000.csv")

#print(df.head(5))
#print(df.tail(5))
#print(df.shape)
#print(len(df))
#print(df.columns)
#print(df.dtypes)
#print(df.isnull())
#print(df["Series_Title"])
#print(df["Series_Title"][:5])
#print(df[["Series_Title", "Released_Year"]])
#print(df.sort_values("Released_Year"))
#print(df["Released_Year"].value_counts())

        ###VERİ FİLTRELEME###

#print(df["IMDB_Rating"][0])
#print(df.loc[df["Series_Title"]=="The Godfather"])
#print(type(df.loc[df["Series_Title"]=="The Godfather"]))
#print(df.loc[df["Series_Title"]=="The Godfather"]["IMDB_Rating"])
#print(df.loc[(df["IMDB_Rating"] >= 8) & (df["No_of_Votes"] >= 100000)])

        ###OBJEYİ SAYIYA ÇEVİRME###
"""
print(type(df["Gross"][0]))
df["Gross"] = df["Gross"].str.replace(",","")
df["Gross"] = pd.to_numeric(df["Gross"])
print(type(df["Gross"][0]))
print(df.loc[(df["IMDB_Rating"] >= 9) & (df["Gross"] >= 100000000)])
"""
        ###MANUEL DATAFRAME OLUŞTURMA###
"""
import random

randomList1 = random.sample(range(15, 25), 2)
randomList2 = random.sample(range(15, 25), 2)

print(randomList1, randomList2)
randomListofList = [randomList1, randomList2]
print("\n", randomListofList)
columns = ["Sıcaklık_1.Gün", "Sıcaklık_2.Gün"]
myDataFrame = pd.DataFrame(randomListofList, index=["İstanbul", "Hatay"], columns=columns)
print("\n", myDataFrame)
print("\n", type(myDataFrame))
"""

        ###İKİNCİ DERS###

#df_kopya = df.copy()
"""
df_yeni = df.drop(["Overview", "Meta_score"], axis=1) #axis=0 satır siler, default 0
print(df_yeni.head())
"""
"""
df_filtered = df[df["IMDB_Rating"] >= 9]
print(df_filtered)
"""
"""
df_filtered = df.query("IMDB_Rating >= 9")
print(df_filtered)
"""
"""
f = lambda x: (x["Runtime"].split())[0]
df["RuntimeYeni"] = df.apply(f, axis=1)
#print(df.head())
df["RuntimeYeni2"] = df["RuntimeYeni"].astype("int")
df.filtered = df.query("RuntimeYeni2 >= 140")
print(df.filtered)
print(df.dtypes)
"""
