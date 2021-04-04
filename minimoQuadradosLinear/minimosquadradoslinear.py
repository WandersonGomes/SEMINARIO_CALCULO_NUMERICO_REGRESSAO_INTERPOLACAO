from ponto import Ponto

class MinimosQuadradosLinear:
    _listaPontos = []
    _somaX = 0
    _somaY = 0
    _somaXY = 0
    _somaXX = 0
    _coeficienteA = 0
    _coeficienteB = 0

    def __init__(self, listaPontos):
        self._listaPontos = listaPontos
        self._somaX = self.calculaSomaX(self._listaPontos)
        self._somaY = self.calculaSomaY(self._listaPontos)
        self._somaXY = self.calculaSomaXY(self._listaPontos)
        self._somaXX = self.calculaSomaXX(self._listaPontos)
        
        self._coeficienteA = self.calculaCoeficienteA()
        self._coeficienteB = self.calculaCoeficienteB()

    def calculaSomaX(self, listaPontos):
        soma = 0
        for ponto in listaPontos:
            soma += ponto.getX()
        return soma
    
    def calculaSomaY(self, listaPontos):
        soma = 0
        for ponto in listaPontos:
            soma += ponto.getY()
        return soma
    
    def calculaSomaXY(self, listaPontos):
        soma = 0
        for ponto in listaPontos:
            soma += (ponto.getX() * ponto.getY())
        return soma
    
    def calculaSomaXX(self, listaPontos):
        soma = 0
        for ponto in listaPontos:
            soma += (ponto.getX() * ponto.getX())
        return soma
    
    def getListaPontos(self):
        return self._listaPontos

    def getSomaX(self):
        return self._somaX
    
    def getSomaY(self):
        return self._somaY

    def getSomaXY(self):
        return self._somaXY
    
    def getSomaXX(self):
        return self._somaXX
    
    def calculaCoeficienteA(self):
        quantidadePontos = len(self._listaPontos)
        
        numerador = ((quantidadePontos * self._somaXY) - (self._somaX * self._somaY)) 
        denominador = ((quantidadePontos * self._somaXX) - (self._somaX * self._somaX))
        
        return numerador/denominador
    
    def calculaCoeficienteB(self):
        quantidadePontos = len(self._listaPontos)
        
        numerador = ((self._somaX * self._somaXY) - (self._somaY * self._somaXX))
        denominador = ((self._somaX * self._somaX) - (quantidadePontos * self._somaXX))
        
        return numerador/denominador
    
    def getCoeficienteA(self):
        return self._coeficienteA
    
    def getCoeficienteB(self):
        return self._coeficienteB
    
    def getFuncao(self):
        return f'{self._coeficienteA}x + {self._coeficienteB}'