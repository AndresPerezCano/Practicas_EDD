class Equipo:

    def __init__(self, nombre, NoPlaca, fecha, valor, empleado):
        self._nombre = nombre
        self._NoPlaca = NoPlaca
        self._fecha = fecha
        self._valor = valor
        self._empleado = empleado

    def __str__(self):
        return f"{self.getNombre()} {self.getNoPlaca()} {self.getFecha().getDia():02d} {self.getFecha().getMes():02d} {self.getFecha().getA():02d} {self.getValor()}"

    #getters
    def getNombre(self):
        return self._nombre

    def getNoPlaca(self):
        return self._NoPlaca

    def getFecha(self):
        return self._fecha

    def getValor(self):
        return self._valor
    
    def getEmpleado(self):
        return self._empleado
    
    #setters
    def setNombre(self, nombre):
        self._nombre = nombre

    def setNoPlaca(self, NoPlaca):
        self._NoPlaca = NoPlaca

    def setFecha(self, fecha):
        self._fecha = fecha

    def setValor(self, valor):
        self._valor = valor
    
    def setEmpleado(self, empleado):
        self._empleado = empleado

    
    
