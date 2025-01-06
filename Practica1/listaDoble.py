# import 
from nodoDoble import NodoDoble
from direccion import Direccion
from usuario import Usuario
from fecha import Fecha

# clase
class ListaDoble():

    # Constructor
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    # Métodos
    def size(self):
        return self._size
    
    def isEmpty(self):
        if self.size() == 0:
            return True
        else: 
            return False
        
    def first(self):
        return self._head
    
    def last(self):
        return self._tail
    
    def addFirst(self, objeto):
        if self.isEmpty():
            self._head = NodoDoble(objeto)
            self._tail = self._head
            self._size += 1
        else: 
            temp = self._head
            self._head = NodoDoble(objeto)
            self._head.setNext(temp)
            temp.setPrev(self._head)
            self._size += 1

    def addLast(self, objeto):
        temp = self._tail
        self._tail = NodoDoble(objeto)
        self._tail.setPrev(temp)
        temp.setNext(self._tail)
        self._size += 1

    def removeFirst(self):
        temp = self._head
        self._head = temp.getNext()
        self._head.setPrev(None)
        temp.setNext(None)

    def remove(self, valor):
        temp = self.first()
        while temp.getData()!=valor:
            temp = temp.getNext()
        if temp.getPrev()==None:
            self._head = temp.getNext()
            self._head.setPrev(None)
            temp.setNext(None)
        elif temp.getNext()==None:
            self._tail = temp.getPrev()
            self._tail.setNext(None)
            temp.setPrev(None)
        else:
            prev = temp.getPrev()
            next = temp.getNext()
            prev.setNext(next)
            next.setPrev(prev)
            temp.setNext(None)
            temp.setPrev(None)

        return temp

    def addAfter(self, indice, valor):
        temp = self.first()
        for i in range(0, indice, 1):
            temp = temp.getNext()
        next = temp.getNext()
        nuevo = NodoDoble(valor)
        temp.setNext(nuevo)
        next.setPrev(nuevo)
        nuevo.setPrev(temp)
        nuevo.setNext(next)
        self._size += 1


if __name__ == "__main__":
    # Ejercicio números ---------------------------------------------------------------------------------------------
    listaDoble = ListaDoble()
    listaDoble.addFirst(1)
    for i in range(2, 21, 2):
        listaDoble.addLast(i)

    print("Lista doble tiene: ")
    temp = listaDoble.first()
    condicion = temp.getNext()
    while condicion!=None:
        print(temp.getData())
        condicion = temp.getNext()
        temp = temp.getNext()

    print("Eliminamos: ")
    listaDoble.remove(1)
    listaDoble.remove(10)
    listaDoble.remove(20)

    temp = listaDoble.first()
    condicion = temp.getNext()
    while condicion!=None:
        print(temp.getData())
        condicion = temp.getNext()
        temp = temp.getNext()

    # Ejercicio Usuarios ------------------------------------------------------------------------------------------
    print("\nEjercicio usuarios: ")
    listaDobleUsuarios = ListaDoble()
    # Creación usuarios
    miFecha = Fecha(24, 7, 2005)
    miDir = Direccion()
    miDir.setCiudad("Bello")
    miDir.setBarrio("Trapiche")
    miDir.setCalle(57)
    miDir.setNomenclatura(6927)
    miDir.setEdificio(16)
    miDir.setApto("1359")
    miUsuario = Usuario("Daniel", 666, 5435355, miFecha, "danzapata@unal", miDir, "Medellin")
    listaDobleUsuarios.addFirst(miUsuario)

    miFecha = Fecha(24, 7, 2005)
    miDir = Direccion()
    miDir.setCiudad("Medellin")
    miDir.setBarrio("Candelaria")
    miDir.setCalle(53)
    miDir.setNomenclatura(3212)
    miDir.setEdificio(1)
    miDir.setApto("412")
    miUsuario = Usuario("juan", 777, 2415433, miFecha, "zjuanR@gmail", miDir, "medellin")
    listaDobleUsuarios.addLast(miUsuario)

    miFecha = Fecha(24, 7, 2005)
    miDir = Direccion()
    miDir.setCiudad("Bello")
    miDir.setBarrio("barrio-nuevo")
    miDir.setCalle(27)
    miDir.setNomenclatura(2423)
    miDir.setEdificio("")
    miDir.setApto("")
    miUsuario = Usuario("Jose", 999, 4421414, miFecha, "nel@unal.edu", miDir, "Medellin")
    listaDobleUsuarios.addLast(miUsuario)

    miFecha = Fecha(24, 7, 2005)
    miDir = Direccion()
    miDir.setCiudad("Envigado")
    miDir.setBarrio("Santa-ana")
    miDir.setCalle(27)
    miDir.setNomenclatura(2423)
    miDir.setEdificio("")
    miDir.setApto("")
    miUsuario = Usuario("Esteban", 121, 444, miFecha, "ban@unal.edu", miDir, "Rionegro")
    listaDobleUsuarios.addLast(miUsuario)

    temp = listaDobleUsuarios.first()
    condicion = temp.getNext()
    while condicion!=None:
        print(temp.getData())
        condicion = temp.getNext()
        temp = temp.getNext()
    
    print("Crea tu usuario: ")
    miUsuario = Usuario(input("Nombre: "), int(input("Numero de documento: ")))
    miUsuario.setTel(int(input("Número de telefono: ")))
    print("Fecha de nacimiento")
    miFecha = Fecha(int(input("Dia: ")), int(input("Mes: ")), int(input("Año: ")))
    miUsuario.setFecha_Nacimiento(miFecha)
    miUsuario.setCiudad_nacimiento(input("Ingrese ciudad de nacimiento: "))
    miUsuario.setEmail(input("Correo electrónico: "))
    miDir = Direccion()
    print("Información de residencia.")
    miDir.setCiudad(input("Ciudad en donde vive: "))
    miDir.setBarrio(input("Barrio: "))
    miDir.setCalle(input("Calle: "))
    miDir.setNomenclatura(input("Nomenclatura: "))
    miDir.setEdificio(input("Edificio: "))
    miDir.setApto(input("Apartamento: "))
    miUsuario.setDir(miDir)

    listaDobleUsuarios.addFirst(miUsuario)

    print("Crea un segundo usuario: ")
    miUsuario = Usuario(input("Nombre: "), int(input("Numero de documento: ")))
    miUsuario.setTel(int(input("Número de telefono: ")))
    print("Fecha de nacimiento")
    miFecha = Fecha(int(input("Dia: ")), int(input("Mes: ")), int(input("Año: ")))
    miUsuario.setFecha_Nacimiento(miFecha)
    miUsuario.setCiudad_nacimiento(input("Ingrese ciudad de nacimiento: "))
    miUsuario.setEmail(input("Correo electrónico: "))
    miDir = Direccion()
    print("Información de residencia.")
    miDir.setCiudad(input("Ciudad en donde vive: "))
    miDir.setBarrio(input("Barrio: "))
    miDir.setCalle(input("Calle: "))
    miDir.setNomenclatura(input("Nomenclatura: "))
    miDir.setEdificio(input("Edificio: "))
    miDir.setApto(input("Apartamento: "))
    miUsuario.setDir(miDir)

    listaDobleUsuarios.addAfter(3, miUsuario)

    temp = listaDobleUsuarios.first()
    condicion = temp.getNext()
    while condicion!=None:
        print(temp.getData())
        condicion = temp.getNext()
        temp = temp.getNext()