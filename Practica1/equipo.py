class Equipo:

    def __init__(self, nombre, NoPlaca, fecha, valor):
        self._nombre = nombre
        self._NoPlaca = NoPlaca
        self._fecha = fecha
        self._valor = valor

    #getters
    def getNombre(self):
        return self._nombre

    def getNoPlaca(self):
        return self._NoPlaca

    def getFecha(self):
        return self._fecha

    def getValor(self):
        return self._valor
    
    #setters
    def setNombre(self, nombre):
        self._nombre = nombre

    def setNoPlaca(self, NoPlaca):
        self._NoPlaca = NoPlaca

    def setFecha(self, fecha):
        self._fecha = fecha

    def setValor(self, valor):
        self._valor = valor

    
    
