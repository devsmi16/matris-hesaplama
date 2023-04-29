import numpy as np

a1 = np.random.randint(5, size=(5, 5))
np.array([[0, 1, 3, 2, 1],
          [4, 3, 2, 2, 1],
          [4, 1, 2, 3, 4],
          [3, 0, 1, 2, 4],
          [2, 0, 1, 2, 3]])

a2 = np.random.randint(7, size=(5, 5))
np.array([[1, 2, 6, 4, 3],
          [2, 4, 5, 5, 0],
          [3, 5, 6, 7, 1],
          [4, 6, 7, 3, 0],
          [5, 6, 7, 3, 2]])

result = np.zeros((5, 4))
for i in range(a1.shape[0]):
    for j in range(a2.shape[1]):
        for k in range(a2.shape[0]):
            result[i][j] += a1[i, k] * a2[k, j]



def transpozAl(matris):
    sutun = []
    sonMatris = []
    s = 0
    m = 0
    while s < len(matris[0]):  # ilk while döngüsü
        sutun = []
        m = 0
        while m < len(matris):  # ikinci while döngüsü
            sutun.append(matris[m][s])
            m = m + 1
        sonMatris.append(sutun)
        s = s + 1
    return sonMatris


matris2 = [[2, 6, 5], [5, 6, 8], [769, 6, 0]]
print(matris2)
print(transpozAl(matris2))
