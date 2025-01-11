# import 
from nodoDoble import NodoDoble

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
        if self.isEmpty():
            self._head = NodoDoble(objeto)
            self._tail = self._head
            self._size += 1

        else:
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

