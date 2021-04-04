def determinante3(matriz):
    parte1 = matriz[0][0] * matriz[1][1] * matriz[2][2]
    parte1 += matriz[0][1] * matriz[1][2] * matriz[2][0]
    parte1 += matriz[0][2] * matriz[1][0] * matriz[2][1]

    parte2 = matriz[0][2] * matriz[1][1] * matriz[2][0]
    parte2 += matriz[0][0] * matriz[1][2] * matriz[2][1]
    parte2 += matriz[0][1] * matriz[1][0] * matriz[2][2]

    return parte1 - parte2