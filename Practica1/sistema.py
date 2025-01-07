from usuario import Usuario
from fecha import Fecha
from equipo import Equipo
from direccion import Direccion
from administrador import Administrador
from investigador import Investigador
from listaDoble import ListaDoble
from listaSimple import ListaSimple
from nodoSimple import NodoSimple

class Sistema:
    
    def __init__(self):
        self._empleados = ListaSimple()
        self._equipos = ListaDoble()

   # def agregarUsuario()

    def accesoSistema(self, cedula, contraseña):
        archivoPassword = open("Practica1/archivos/Password.txt","r")
        while True:
            password = archivoPassword.readline()
            password = password.strip()
            if not password:
                archivoPassword.close()
                print("El documento no esta registrado")
                break
            else:
                cedulaP,contraseñaP,descripcion = password.split(" ")
                if cedula == int(cedulaP):
                    if contraseña == contraseñaP:
                        archivoPassword.close()
                        if descripcion == "administrador":
                            print("Ingreso como administrador concedido")
                            self.accesoAdministrador(int(cedula))
                            break
                        
                        elif descripcion == "investigador":
                            print("Ingreso como investigador concedido")
                            self.accesoInvestigador(int(cedula))
                            break

                    else:
                        archivoPassword.close()
                        print("Contraseña incorrecta")
                        break
                
    def accesoAdministrador(self, cedula):
        indice = self.busqueda(cedula)
        empleado = self._empleados[indice]
        pass

    def accesoInvestigador(self, cedula):
        empleado = self.busqueda(cedula,"empleado-ID")
        while True:
            print("Que proceso desea realizar:")
            print("1.Consultar mis equipos.")
            print("2.Salir.")
            indice = int(input("Ingrese un indice:"))
            if indice == 1:
                empleado.getData().consultaEquipos()
                indice12 = input("Desea realizar otra accion si/no:")
                if indice12 == "si":
                    pass
                elif indice12 == "no":
                    break
            
            elif indice == 2:
                break
            
            else:
                print("Indice no valido")
        

    def busqueda(self, dato,tipo):
        temp = self._empleados.first()
        if tipo == "empleado-nombre":
            while(temp != None and temp.getData().getNombre() != dato):
                temp = temp.getNext()
            return temp
        
        elif tipo == "empleado-ID":
            while(temp != None and temp.getData().getId() != dato):
                temp = temp.getNext()
            return temp

        

        




if __name__ == "__main__":

    sistema = Sistema()

    archivoEmpleados = open("Practica1/archivos/Empleados.txt","r")
    while True:
        usuario = archivoEmpleados.readline()
        usuario = usuario.strip()
        if not usuario:
            break
        else:
            nombre,id,fecha_nacimiento,ciudad_nacimiento,tel,email,dir = usuario.split("/")
            dia, mes, año = fecha_nacimiento.split("-")
            ciudad,calle,nomenclatura,barrio,edificio,apto = dir.split(" ")  
            
            archivoPassword = open("Practica1/archivos/Password.txt","r")
            
            while True:
                descripcion = archivoPassword.readline()
                descripcion = descripcion.strip()
                if not descripcion:
                    break
                else:
                    cedulaP,contraseñaP,descripcion1 = descripcion.split(" ")
                    if id == cedulaP:
                        if descripcion1 == "administrador":
                            usuario1 = Administrador(nombre,id,Fecha(int(dia),int(mes),int(año)),ciudad_nacimiento,tel,email,Direccion(calle,ciudad,nomenclatura,barrio,edificio,apto))
                            sistema._empleados.addFirst(usuario1)
                        
                        elif descripcion1 == "investigador":
                            usuario1 = Investigador(nombre,id,Fecha(int(dia),int(mes),int(año)),ciudad_nacimiento,tel,email,Direccion(calle,ciudad,nomenclatura,barrio,edificio,apto))
                            sistema._empleados.addFirst(usuario1)
                

    archivoPassword.close()

    archivoEquipos = open("Practica1/archivosOp/inventarioInicial.txt","r")
    while True:
        equipo = archivoEquipos.readline()
        equipo = equipo.strip()
        if not equipo:
            break
        else:
            empleado,cedula,nombre,NoPlaca,dia,mes,año,valor = equipo.split(" ")
            empleado1 = sistema.busqueda(empleado,"empleado-nombre").getData()
            equipo1 = Equipo(nombre,NoPlaca,Fecha(int(dia),int(mes),int(año)),valor,empleado1)
            empleado1.agregarEquipo(equipo1)
            sistema._equipos.addFirst(equipo1)


    archivoEquipos.close()

    cedula = int(input("Ingrese su documento: "))
    contraseña = input("Ingrese su contraseña: ")
    sistema.accesoSistema(cedula,contraseña)

    #pruebas



    