from usuario import Usuario
from listaDoble import ListaDoble

class Investigador(Usuario):

    def __init__(self,nombre,cedula,fecha,ciudad_nacimiento,tel,email,direccion,equipos=None):
        super().__init__(nombre,int(cedula),fecha,ciudad_nacimiento,tel,email,direccion)
        self._equipos = ListaDoble()

    #Metodos
    def agregarEquipo(self, equipo):
        self._equipos.addLast(equipo)

    def consultaEquipos(self):
        temporal = self._equipos.first()
        if temporal != None:
            print("______________________________________________________________________________________________________________________")
            print("Equipos a nombre de ",self.getNombre(),":",sep="")
            while temporal != None:
                print("*",temporal.getData(),sep="")
                temporal = temporal.getNext()
            print("______________________________________________________________________________________________________________________")
        
        else:
            print("No hay equipos a nombre de ",self.getNombre(),":",sep="")

    def adicionarEquipo(self):
        print("Ingrese los siguientes datos con espacios de por medio:")
        datos = input("nombre del equipo - No.Placa - fecha de compra(dia mes año) - valor de compra: ")
        nombreE,NoPlaca,dia,mes,año,valor = datos.split(" ")
        archivo = open("Practica1/archivosSistema/solicitudes.txt", "a")
        archivo.write(f"\n{self._nombre} {self._id} {nombreE} {NoPlaca} {dia} {mes} {año} {valor} agregar pendiente")
        archivo.close()
        print("Solicitud realizada con exito: ")
    
    def eliminarEquipo(self,lista):
        codigo = int(input("Ingrese el codigo del equipo: "))
        descripcion = input("Escriba una breve explicacion de porque se desea eliminar: ")
        archivo = open("Practica1/archivosSistema/solicitudes.txt", "a")
        archivo.write(f"\n{self._nombre} {self._id} {codigo} {descripcion.replace(' ','_')} eliminar pendiente")
        archivo.close()
        temp = lista.first()
        while temp != None:
            if codigo != int(temp.getData().getNoPlaca()):
                temp = temp.getNext()
            else:
                break
        equipo = temp.getData()
        archivo1 = open("Practica1/archivosSistema/equiposEliminados.txt", "a")
        archivo1.write(f"\n{self._nombre} {self._id} {equipo.getNombre()} {equipo.getNoPlaca()} {equipo.getFecha().getDia():02d} {equipo.getFecha().getMes()} {equipo.getFecha().getA()} {equipo.getValor()} {descripcion.replace(' ','_')}eliminar pendiente")
        archivo.close()
        print("Solicitud realizada con exito: ")

    def consultaEstadoSolicitudes(self):
        archivo = open("Practica1/archivosSistema/solicitudes.txt", "r")
        print("______________________________________________________________________________________________________________________")
        print("Estado solicitudes: ")
        while True:
            solicitud = archivo.readline()
            solicitud = solicitud.strip()
            if not solicitud:
                archivo.close()
                break
            else:
                solicitud = solicitud.split(" ")
                if int(solicitud[1]) == self._id:
                    if len(solicitud) == 6 or len(solicitud) == 12:
                        historialI = open("Practica1/archivosSistema/equiposEliminados.txt","r")
                        while True:
                            equipo = historialI.readline()
                            equipo = equipo.strip()
                            if not equipo:
                                historialI.close()
                                break
                            else:
                                codigo = equipo.split(" ")[3]
                                if codigo == solicitud[2]:
                                    print(f"* {self._nombre} {self._id}",*equipo.split(" ")[2:8],*equipo.split(" ")[9:])
                            
                    elif len(solicitud) == 10 or len(solicitud) == 16:
                        print("*",*solicitud[:10],)
        print("______________________________________________________________________________________________________________________")
       
    def archivoInventario(self):
        temp = self._equipos.first()
        inventario = open(f"Practica1/archivos/{self._nombre} {self._id}.txt","w")
        while temp != None:
            inventario.write(f"{temp.getData()}\n")
            temp = temp.getNext()        
        inventario.close()
    
    def archivoSolicitudes(self):
        archivo = open("Practica1/archivosSistema/solicitudes.txt", "r")
        archivoSolicitudes = open(f"Practica1/archivos/solicitudes {self._nombre} {self._id}.txt","w")
        while True:
            solicitud = archivo.readline()
            solicitud = solicitud.strip()
            if not solicitud:
                archivo.close()
                break
            else:
                listaSolicitud = solicitud.split(" ")
                if int(listaSolicitud[1]) == self._id:
                    if len(listaSolicitud) == 6 or len(listaSolicitud) == 12:
                        
                        historialI = open("Practica1/archivosSistema/equiposEliminados.txt","r")
                        while True:
                            equipo = historialI.readline()
                            equipo = equipo.strip()
                            if not equipo:
                                historialI.close()
                                break
                            else:
                                codigo = equipo.split(" ")[3]
                                if codigo == listaSolicitud[2]:
                                    stringEquipo = " ".join(equipo.split(" ")[2:8])
                                    archivoSolicitudes.write(f"{self._nombre} {self._id} {stringEquipo} eliminar aceptar\n")
                            
                    elif len(listaSolicitud) == 10 or len(listaSolicitud) == 16:
                        string = " ".join(listaSolicitud[:10])
                        archivoSolicitudes.write(f"{string}\n")
                
        archivoSolicitudes.close()

                    
                    


                            

    




