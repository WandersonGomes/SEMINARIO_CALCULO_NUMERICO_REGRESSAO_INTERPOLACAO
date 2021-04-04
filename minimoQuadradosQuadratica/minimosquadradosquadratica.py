from ponto import Ponto
from determinantes import determinante3

class MinimosQuadradosQuadratica:
    _listaPontos = []
    _somaX = 0
    _somaXX = 0
    _somaXXX = 0
    _somaXXXX = 0
    _somaY = 0
    _somaXY = 0
    _somaXXY = 0
    _coeficienteA = 0
    _coeficienteB = 0
    _coeficienteC = 0
    _determinante = 0
    _matriz = []

    def __init__(self, listaPontos):
        self._listaPontos = listaPontos

        self._somaX = self.calculaSomaX(self._listaPontos)
        self._somaXX = self.calculaSomaXX(self._listaPontos)
        self._somaY = self.calculaSomaY(self._listaPontos)

        self._somaXXX = self.calculaSomaXXX(self._listaPontos)
        self._somaXY = self.calculaSomaXY(self._listaPontos)
        
        self._somaXXXX = self.calculaSomaXXXX(self._listaPontos)
        self._somaXXY = self.calculaSomaXXY(self._listaPontos)

        self._matriz.append([len(listaPontos), self._somaX, self._somaXX])
        self._matriz.append([self._somaX, self._somaXX, self._somaXXX])
        self._matriz.append([self._somaXX, self._somaXXX, self._somaXXXX])
        self._determinante = determinante3(self._matriz)

        self._coeficienteA = self.calculaCoeficienteA()
        self._coeficienteB = self.calculaCoeficienteB()
        self._coeficienteC = self.calculaCoeficienteC()

    def calculaSomaX(self, listaPontos):
        soma = 0
        for ponto in listaPontos:
            soma += ponto.getX()
        return soma
    
    def calculaSomaXX(self, listaPontos):
        soma = 0
        for ponto in listaPontos:
            soma += (ponto.getX() * ponto.getX())
        return soma

    def calculaSomaY(self, listaPontos):
        soma = 0
        for ponto in listaPontos:
            soma += ponto.getY()
        return soma
    
    def calculaSomaXXX(self, listaPontos):
        soma = 0
        for ponto in listaPontos:
            soma += (ponto.getX() * ponto.getX() * ponto.getX())
        return soma

    def calculaSomaXY(self, listaPontos):
        soma = 0
        for ponto in listaPontos:
            soma += (ponto.getX() * ponto.getY())
        return soma
    
    def calculaSomaXXXX(self, listaPontos):
        soma = 0
        for ponto in listaPontos:
            soma += (ponto.getX() * ponto.getX() * ponto.getX() * ponto.getX())
        return soma

    def calculaSomaXXY(self, listaPontos):
        soma = 0
        for ponto in listaPontos:
            soma += (ponto.getX() * ponto.getX() * ponto.getY())
        return soma
     
    def calculaCoeficienteC(self):
        linha1 = [self._somaY, self._somaX, self._somaXX]
        linha2 = [self._somaXY, self._somaXX, self._somaXXX]
        linha3 = [self._somaXXY, self._somaXXX, self._somaXXXX]

        return determinante3([linha1, linha2, linha3])/self._determinante
    
    def calculaCoeficienteB(self):
        linha1 = [len(self._listaPontos), self._somaY, self._somaXX]
        linha2 = [self._somaX, self._somaXY, self._somaXXX]
        linha3 = [self._somaXX, self._somaXXY, self._somaXXXX]

        return determinante3([linha1, linha2, linha3])/self._determinante

    def calculaCoeficienteA(self):
        linha1 = [len(self._listaPontos), self._somaX, self._somaY]
        linha2 = [self._somaX, self._somaXX, self._somaXY]
        linha3 = [self._somaXX, self._somaXXX, self._somaXXY]

        return determinante3([linha1, linha2, linha3])/self._determinante

    def getFuncao(self):
        return f'{self._coeficienteA}x^2 + {self._coeficienteB}x + {self._coeficienteC}'