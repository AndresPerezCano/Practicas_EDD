class Usuario:
    
    def __init__(self,nombre=None,id=None,fecha_nacimiento=None,ciudad_nacimiento=None,tel=None,email=None,dir=None):
        self._nombre = nombre
        self._id = id
        self._fecha_nacimiento = fecha_nacimiento
        self._ciudad_nacimiento = ciudad_nacimiento
        self._tel = tel
        self._email = email
        self._dir = dir
    
    def setNombre(self, n):
        self._nombre = n

    def setId(self, id):
        self._id = id

    def setFecha_nacimiento(self, f):
        self._fecha_nacimiento = f

    def setCiudad_nacimiento(self, c):
        self._ciudad_nacimiento = c
   
    def setTel(self, t):
        self._tel = t
        
    def setEmail(self, e):
        self._email = e

    def setDir(self, d):
        self._dir = d
    
    def getNombre(self):
        return self._nombre 

    def getId(self):
        return self._id

    def getFecha_nacimiento(self):
        return self._fecha_nacimiento
   
    def getCiudad_nacimiento(self):
        return self._ciudad_nacimiento
    
    def getTel(self):
        return self._tel
    
    def getEmail(self):
        return self._email

    def getDir(self):
        return self._dir

    def __str__(self):
        return f"{self.getNombre()}/{self.getId()}/{self.getFecha_nacimiento().getDia():02d}-{self.getFecha_nacimiento().getMes():02d}-{self.getFecha_nacimiento().getA():02d}/{self.getCiudad_nacimiento()}/{self.getTel()}/{self.getEmail()}/{self.getDir()}"