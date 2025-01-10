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
        temporal = self._equipos.first()
        if temporal != None:
            print("_____________________________________________________________________________________________________________________________________")
            print("Equipos a nombre de ",self.getNombre(),":",sep="")
            while temporal.getNext() != None:
                print("*",temporal.getData(),sep="")
                temporal = temporal.getNext()
            print("_____________________________________________________________________________________________________________________________________")
        else:
            print("No hay equipos a nombre de ",self.getNombre(),":",sep="")

    def generarDocInventario(self, usuario):
        nombre = usuario.getNombre()
        cedula = usuario.getId()
        t = open(f"Practica1/archivosOp/{nombre} {cedula}.txt", "w")

        temp = usuario._equipos.first()
        while temp != None:
            if temp != usuario._equipos.last():
                t.write(f"{temp.getData().__str__()}\n")
            else:
                t.write(temp.getData().__str__())
            temp = temp.getNext()