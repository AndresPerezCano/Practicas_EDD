from usuario import Usuario

class Investigador(Usuario):

    def __init__(self,nombre,cedula,fecha,ciudad_nacimiento,tel,email,direccion,equipos=None):
        super().__init__(nombre,cedula,fecha,ciudad_nacimiento,tel,email,direccion)
        self._equipos = []

    def agregarEquipo(self, equipo):
        self._equipos.append(equipo)
    pass