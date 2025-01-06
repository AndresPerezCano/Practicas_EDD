# Clase 
class NodoDoble:
    
    # Constructor
    def __init__(self, data = None):
        self._data = data
        self._next = None
        self._prev = None

    # Métodos
    def setData(self, data):
        self._data = data
    
    def setNext(self, node):
        self._next = node

    def setPrev(self, node):
        self._prev = node

    def getData(self):
        return self._data
    
    def getNext(self):
        return self._next
    
    def getPrev(self):
        return self._prev