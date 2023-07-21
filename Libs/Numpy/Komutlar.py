import numpy as np
"""
a = np.array([1, 5, 10])
print(a)

b = np.array([[2, 5, 8], [5, 8, 9]])
print(b)

print(b.ndim)
print(b.shape)
print(b.dtype)
print(b[0, 2])
print(b[0, 1:])
"""
        ###OTOMATİK DİZİ OLUŞTURMA###
"""
dizi_s = np.zeros((2, 3))
print(dizi_s)

dizi1 = np.full((4, 4), 50)
print(dizi1)

dizi2 = np.random.rand(4, 3)
print(dizi2)

dizi3 = np.random.randint(0, 10, size=(5, 5))
print(dizi3)
"""
        ###DİZİ KOPYALAMA###
"""
c = np.array([1, 2, 3])
d = c
d[0] = 90
print(c)

e = np.array([1, 2, 3])
f = e.copy()
f[0] = 90
print(e)
"""
        ###DİZİLERDE MATEMATİKSEL İŞLEMLER###
"""
a = np.array([1, 2, 3])
print(4-a)
"""
        ###İSTATİSTİK###
""""
dizi4 = np.array([[1, 2, 3], [4, 5, 6]])

print(np.min(dizi4))
print(np.max(dizi4))
print(np.sum(dizi4))
"""
        ###DOSYADAN DİZİ YÜKLEME###
"""
filedata = np.genfromtxt("ornek.txt", delimiter=",")
filedata = filedata.astype("int32")
print(filedata)
"""
