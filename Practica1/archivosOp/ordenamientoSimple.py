import random

from listaSimple import ListaSimple

class Ordenador_Lista:
    
    def __init__(self):
        self._lista = ListaSimple()

    def inicializar(self, n):
        while n > 0:
            numero = random.randint(-5000,5000)
            self._lista.agregarUltimo(numero)
            n -= 1

    def ordenar(self):
        nodo = self._lista.primero()
        while nodo:
            nodo2 = nodo.getSiguiente()
            while nodo2:
                if nodo.getDato() > nodo2.getDato():
                    self.intercambiar(nodo,nodo2)
                nodo2 = nodo2.getSiguiente()
            nodo = nodo.getSiguiente()
    
    def intercambiar(self,primero,segundo):
        temporal = primero.getDato()
        primero.setDato(segundo.getDato())
        segundo.setDato(temporal)
        
    def mostrar(self):
        nodo = self._lista.primero()
        indice = self._lista.tamaño()
        print("[",end=" ")
        while indice > 0:
            print(nodo.getDato(),end=" ")
            nodo = nodo.getSiguiente()
            indice -= 1
        print("]")

if __name__ == "__main__":
    ordenador = Ordenador_Lista()
    ordenador.inicializar(12)
    #ordenador.mostrar()
    ordenador.ordenar()
    ordenador.mostrar()
    
