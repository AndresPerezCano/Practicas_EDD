from usuario import Usuario
from fecha import Fecha
from equipo import Equipo
from direccion import Direccion

class Sistema:
    
    def __init__(self):
        self._empleados = []
        self._equipos = []

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
            usuario1 = Usuario(nombre,id,Fecha(int(dia),int(mes),int(año)),ciudad_nacimiento,tel,email,Direccion(calle,ciudad,nomenclatura,barrio,edificio,apto))
            sistema._empleados.append(usuario1)

    archivoEmpleados.close()

    archivoEquipos = open("Practica1/archivosOp/inventarioInicial.txt","r")
    while True:
        equipo = archivoEquipos.readline()
        equipo = equipo.strip()
        if not equipo:
            break
        else:
            empleado,cedula,nombre,NoPlaca,dia,mes,año,valor = equipo.split(" ")
            indice1 = sistema.busqueda(empleado)
            print(indice1)
            empleado1 = sistema._empleados[indice1]
            equipo1 = Equipo(nombre,NoPlaca,Fecha(dia,mes,año),valor,empleado1)
            empleado1.agregarEquipo(equipo1)
            sistema._equipos.append(equipo1)


    archivoEquipos.close()

    print(sistema._equipos)
    print(sistema._empleados[0]._equipos())

    cedula = int(input("Ingrese su documento: "))
    contraseña = input("Ingrese su contraseña: ")
    print(sistema.accesoSistema(cedula,contraseña))





    equipo1 = Equipo("CAMARA_MONOCROMATICA",50109773,Fecha(9, 12, 2021), 786000)

    