from minimosquadradoslinear import MinimosQuadradosLinear
from ponto import Ponto

if __name__ == "__main__":
    quantidadePontos = int(input("Informe a quantidade de pontos: "))

    listaPontos = []
    for i in range(quantidadePontos):
        x = float(input("X: "))
        y = float(input("Y: "))

        ponto = Ponto(x, y)

        listaPontos.append(ponto)
    
    minimoQuadradoLinear = MinimosQuadradosLinear(listaPontos)

    print()
    print("Funcao: ", minimoQuadradoLinear.getFuncao())