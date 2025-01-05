class Direccion:

    def __init__(self,calle,ciudad,nomenclatura,barrio,edificio=None,apto=None):
        self._calle = calle
        self._ciudad = ciudad
        self._nomenclatura = nomenclatura
        self._edificio = edificio
        self._barrio = barrio
        self._apto = apto
    
    def setCalle(self, c):
        self._calle = c
        
    def setNomenclatura(self, n):
        self._nomenclatura = n

    def setBarrio(self, b):
        self._barrio = b

    def setCiudad(self, ci):
        self._ciudad = ci

    def setEdificio(self, e):
        self._edificio = e

    def setApto(self, a):
        self._apto = a

    def getCalle(self):
        return self._calle
        
    def getNomenclatura(self):
        return self._nomenclatura

    def getBarrio(self):
        return self._barrio

    def getCiudad(self):
        return self._ciudad

    def getEdificio(self):
        return self._edificio

    def getApto(self):
        return self._apto
        
    def __str__(self):
        return f"{self._ciudad} {self._calle} {self._nomenclatura} {self._barrio} {self._edificio} {self._apto}"
        