from usuario import Usuario
from listaDoble import ListaDoble

class Administrador(Usuario):

    def __init__(self,nombre,cedula,fecha,ciudad_nacimiento,tel,email,direccion,equipos=None):
        super().__init__(nombre,cedula,fecha,ciudad_nacimiento,tel,email,direccion)
        self._equipos = ListaDoble()

    # Métodos 
    def agregarEquipo(self, equipo):
        self._equipos.addFirst(equipo)

    def registrarUsuario(self, nombre,cedula,fecha,ciudad_nacimiento,tel,email,direccion):
        pass