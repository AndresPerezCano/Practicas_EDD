from listaDoble import ListaDoble
from fecha import Fecha
from direccion import Direccion
from usuario import Usuario

class OrdenadorAgenda:

    def __init__(self):
        self._L = ListaDoble()
    
    def agregarUsuario(self, usuario):
        self._L.agregarUltimo(usuario)

    def ordenar(self):
        nodo = self._L.primero()
        while nodo:
            nodo2 = nodo.getSiguiente()
            while nodo2:
                if nodo.getDato().getId() > nodo2.getDato().getId():
                    self.intercambiar(nodo,nodo2)
                nodo2 = nodo2.getSiguiente()
            nodo = nodo.getSiguiente()
    
    def intercambiar(self,primero,segundo):
        temporal = primero.getDato()
        primero.setDato(segundo.getDato())
        segundo.setDato(temporal)
        

    def mostrar(self):
        nodo = self._L.primero()
        indice = self._L.tamaño()
        print("[")
        while indice > 0:
            print(nodo.getDato())
            nodo = nodo.getSiguiente()
            indice -= 1
        print("]")
    

if __name__ == "__main__":
    ordenador = OrdenadorAgenda()

    archivo = open("Laboratorio5/Agenda.txt","r")
    while True:
        usuario = archivo.readline()
        usuario = usuario.strip()
        if not usuario:
            break
        else:
            nombre,id,fecha_nacimiento,ciudad_nacimiento,tel,email,dir = usuario.split("/")
            dia, mes, año = fecha_nacimiento.split("-")
            ciudad,calle,nomenclatura,barrio,edificio,apto = dir.split(" ")  
            usuario1 = Usuario(nombre,id,Fecha(int(dia),int(mes),int(año)),ciudad_nacimiento,tel,email,Direccion(calle,ciudad,nomenclatura,barrio,edificio,apto))
            ordenador.agregarUsuario(usuario1)

    archivo.close()
    
    ordenador.mostrar()

    ordenador.ordenar()
    
    print("_____________________________________________________________________________________________________________________________________")

    ordenador.mostrar()