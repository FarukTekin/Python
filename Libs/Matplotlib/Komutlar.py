import matplotlib.pyplot as plt
import numpy as np
import pandas
import pandas as pd

#plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
"""
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
plt.title("İsim")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x, y)
"""
"""
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
plt.xticks([1, 2, 3, 4])
plt.yticks([1, 4, 9, 16])
plt.title("İsim")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x, y)
"""
        ###LEJANT KOYMA###
"""
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
plt.plot(x, y, label="x^2", color="red")
plt.xticks([1, 2, 3, 4])
plt.yticks([1, 4, 9, 16])
plt.title("Kare Grafiği")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
"""
"""
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
plt.plot(x, y, label="x^2", color="blue", linewidth=2, linestyle="-", marker=".")
plt.xticks([1, 2, 3, 4])
plt.yticks([1, 4, 9, 16])
plt.title("Kare Grafiği")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
"""
        ###AYNI GRAFİKTE BİRDEN FAZLA ÇİZİM YAPMAK###
"""
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y, label="x^2", color="blue", linewidth=2, linestyle="-", marker=".")
plt.xticks([1, 2, 3, 4, 5])
plt.yticks([1, 4, 9, 16, 25])
plt.title("Kare Grafiği")
plt.xlabel("x axis")
plt.ylabel("y axis")

x2 = np.arange(0, 5.1, 0.5)
plt.plot(x2, x2*2, color="red", linewidth=2, marker=".", label="2*x")
plt.legend()
"""
        ###KAYDETME###
"""
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y, label="x^2", color="blue", linewidth=2, linestyle="-", marker=".")
plt.xticks([1, 2, 3, 4, 5])
plt.yticks([1, 4, 9, 16, 25])
plt.title("Kare Grafiği")
plt.xlabel("x axis")
plt.ylabel("y axis")

x2 = np.arange(0, 5.1, 0.5)
plt.plot(x2, x2*2, color="red", linewidth=2, marker=".", label="2*x")
plt.legend()
plt.savefig("kare_grafiği.png", dpi=300)
"""
        ###BARCHART###
"""
x = ["Adana", "Hatay", "Osmaniye"]
y = [120, 178, 87]
#plt.bar(x, y)

cubuklar = plt.bar(x, y)
cubuklar[2].set_hatch("+")
cubuklar[1].set_hatch("/")
cubuklar[0].set_hatch(".")
"""
"""
plt.show()
"""
        ###DETAYLI ÖRNEKLER###
"""
gas = pd.read_csv("petrolfiyatlari.csv")

plt.title("Petrol Fiyatları")
plt.plot(gas["Year"], gas["USA"], "b.-", label="USA")
plt.plot(gas["Year"], gas["Canada"], "r.-", label="Kanada")
plt.plot(gas["Year"], gas["France"], "y.-", label="Fransa")
plt.plot(gas["Year"], gas["South Korea"], "g.-", label="Güney Kore")

plt.xlabel("Yıl")
plt.ylabel("Dolar")

plt.legend()
plt.show()
"""
"""
gas = pd.read_csv("petrolfiyatlari.csv")

plt.figure(figsize=(10,5))
plt.title("Petrol Fiyatları")
plt.plot(gas["Year"], gas["USA"], "b.-", label="USA")
plt.plot(gas["Year"], gas["Canada"], "r.-", label="Kanada")
plt.plot(gas["Year"], gas["France"], "y.-", label="Fransa")
plt.plot(gas["Year"], gas["South Korea"], "g.-", label="Güney Kore")

plt.xlabel("Yıl")
plt.ylabel("Dolar")

plt.legend()
plt.show()
"""