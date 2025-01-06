from usuario import Usuario
from fecha import Fecha
from equipo import Equipo
from direccion import Direccion
from administrador import Administrador
from investigador import Investigador
from listaDoble import ListaDoble
from listaSimple import ListaSimple

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
                return "El documento no esta registrado"
            else:
                cedulaP,contraseñaP,descripcion = password.split(" ")
                if cedula == int(cedulaP):
                    if contraseña == contraseñaP:
                        archivoPassword.close()
                        if descripcion == "administrador":
                            self.accesoAdministrador(int(cedula))
                        
                        elif descripcion == "investigador":
                            self.accesoInvestigador(int(cedula))

                        return "Ingreso concedido"
                    else:
                        archivoPassword.close()
                        return "Contraseña incorrecta"
                
    def accesoAdministrador(self, cedula):
        indice = self.busqueda(cedula)
        empleado = self._empleados[indice]
        pass

    def accesoInvestigador(self, cedula):
        pass

    def busqueda(self, dato):
        for i in range(len(self._empleados)):
            empleado = self._empleados[i]
            if empleado.getNombre() == dato:
                return i

        




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
            indice100 = sistema.busqueda(empleado)
            empleado1 = sistema._empleados[indice100]
            equipo1 = Equipo(nombre,NoPlaca,Fecha(int(dia),int(mes),int(año)),valor,empleado1)
            empleado1.agregarEquipo(equipo1)
            sistema._equipos.append(equipo1)


    archivoEquipos.close()

    cedula = int(input("Ingrese su documento: "))
    contraseña = input("Ingrese su contraseña: ")
    print(sistema.accesoSistema(cedula,contraseña))


    