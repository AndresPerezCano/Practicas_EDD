# Clase 
class NodoSimple:
    
    # Constructor
    def __init__(self, data = None):
        self._data = data
        self._next = None

    # Métodos
    def setData(self, data):
        self._data = data
    
    def setNext(self, node):
        self._next = node

    def getData(self):
        return self._data
    
    def getNext(self):
        return self._next