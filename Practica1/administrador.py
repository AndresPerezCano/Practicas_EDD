from usuario import Usuario
from listaDoble import ListaDoble

class Administrador(Usuario):

    def __init__(self,nombre,cedula,fecha,ciudad_nacimiento,tel,email,direccion,equipos=None):
        super().__init__(nombre,int(cedula),fecha,ciudad_nacimiento,tel,email,direccion)
        self._equipos = ListaDoble()

    # Métodos 
    def agregarEquipo(self, equipo):
        self._equipos.addFirst(equipo)

    def consultaEquipos(self):
        print("_____________________________________________________________________________________________________________________________________")
        print("Equipos a nombre de ",self.getNombre(),":",sep="")
        temporal = self._equipos.first()
        while temporal.getNext() != None:
            print("*",temporal.getData(),sep="")
            temporal = temporal.getNext()
        print("_____________________________________________________________________________________________________________________________________")
