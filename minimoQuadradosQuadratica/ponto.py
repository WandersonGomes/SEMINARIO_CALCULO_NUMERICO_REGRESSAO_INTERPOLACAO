"""
Ponto
Define um ponto no espaco 2D
"""
class Ponto:
    """
    Class Ponto
    
    ponto1 = Ponto(x, y)
    ponto2 = Ponto(x, y)
    """
    _x = 0
    _y = 0

    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def getX(self):
        return self._x
    
    def getY(self):
        return self._y

    def setX(self, x):
        self._x = x
    
    def setY(self, Y):
        self._y = y