class Fecha:
    
    def __init__(self, dd=None, mm=None, aa=None):
        self._dd = dd
        self._mm = mm
        self._aa = aa

    def setDia(self, dd):
        self._dd = dd
    
    def setMes(self, mm):
        self._mm = mm

    def setA(self, aa):
        self._aa = aa

    def getDia(self):
        return self._dd

    def getMes(self):
        return self._mm

    def getA(self):
        return self._aa