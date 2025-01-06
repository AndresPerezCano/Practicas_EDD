# import
from nodoSimple import NodoSimple

# Clase 
class ListaSimple:

    # Constructor
    def __init__(self):
        self._head = None
        self._tail = None
        self._size =  0
    
    # Métodos
    def size(self):
        return self._size

    def setSize(self, siza):
        self._size = siza

    def isEmpty(self):
        if self._size == 0:
            return True
        else: 
            return False
        
    def first(self):
        return self._head
    
    def last(self):
        return self._tail
    
    def addFirst(self, objeto):
        if self._size == 0:
            self._head = NodoSimple(objeto)
            self._tail = self._head
            self._size += 1
        else:
            temp = self._head
            self._head = NodoSimple(objeto)
            self._head.setNext(temp)
            self._size += 1 

    def addLast(self, objeto):
        temp = self._head
        condicion = temp.getNext()
        while condicion != None:
            temp = temp.getNext()
            condicion = temp.getNext()
        nodo = NodoSimple(objeto)
        temp.setNext(nodo)
        self._tail = nodo
        self._size += 1
    
    def removeFirst(self):
        if self._size == 1 or self._size ==0:
            retorno = self._head
            self._head = None
            return retorno
        else:
            retorno = self._head
            temp = retorno.getNext()
            retorno.setNext(None)
            self._head = temp
            return retorno
        
if __name__ == "__main__":
    lista = ListaSimple()

    contador = 1
    lista.addFirst(contador)
    for i in range(2, 21, 2):
        lista.addLast(i)

    temp = lista._head
    condicion = temp.getNext()
    print("Lista tiene: ")
    while condicion !=None:
        print(temp.getData())
        condicion = temp.getNext()
        temp = temp.getNext()
    
    print("Eliminamos y queda: ")
    
