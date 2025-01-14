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
            print("________________________________________________________________________________________________________________________")
            print("Equipos a nombre de ",self.getNombre(),":",sep="")
            while temporal != None:
                print("*",temporal.getData(),sep="")
                temporal = temporal.getNext()
            print("________________________________________________________________________________________________________________________")
        else:
            print("No hay equipos a nombre de ",self.getNombre(),":",sep="")

    def generarDocInventario(self, usuario):
        nombre = usuario.getNombre()
        cedula = usuario.getId()
        t = open(f"Practica1/archivos/{nombre} {cedula}.txt", "w")

        temp = usuario._equipos.first()
        while temp != None:
            if temp != usuario._equipos.last():
                t.write(f"{temp.getData().__str__()}\n")
            else:
                t.write(temp.getData().__str__())
            temp = temp.getNext()
    
    def generarDocSolicitudes(self, conditional):
        # Generar erchivo solicitudes
        with open("Practica1/archivosSistema/solicitudes.txt","r") as archivo:
            # Creamos el texto
            texto = archivo.read().split("\n")
            textoNuevo = []

            if conditional == 2: # Solis de eliminar--------------------------------
                for i in texto:
                    temp = i.split(" ")
                    guardar = len(temp)
                    if (int(guardar)==6) and (temp[-1]=="pendiente"):
                        concatenar = ""
                        for e in temp:
                            if e == temp[-1]:
                                concatenar+=e
                            else:
                                concatenar+=e+" "
                        textoNuevo.append(concatenar)
                with open("Practica1/archivos/Solicitudes_eliminar.txt", "w") as j:
                    for i in textoNuevo:
                            linea = i.split(" ")
                            stringEmpleado = " ".join(linea[:2])
                            stringfinal = " ".join(linea[4:])
                            historialI = open("Practica1/archivosSistema/inventarioCentroDeInvestigacion.txt","r")
                            stringEquipo = ""
                            while True:
                                equipo = historialI.readline()
                                equipo = equipo.strip()
                                if not equipo:
                                    historialI.close()
                                    break
                                else:
                                    codigo = equipo.split(" ")[3]
                                    if int(codigo) == int(linea[2]):
                                        stringEquipo = " ".join(equipo.split(" ")[2:])
                            j.write(f"{stringEmpleado} {stringEquipo} {stringfinal}\n")
                            
                print("Proceso realizado con éxito")
            elif conditional == 1: # Solis agregar-------------------------
                for i in texto:
                    temp = i.split(" ")
                    guardar = len(temp)
                    if (int(guardar)==10) and (temp[-1]=="pendiente"):
                        concatenar = ""
                        for e in temp:
                            if e == temp[-1]:
                                concatenar+=e
                            else:
                                concatenar+=e+" "
                        textoNuevo.append(concatenar)
                with open("Practica1/archivos/Solicitudes_agregar.txt", "w") as j:
                    for i in textoNuevo:
                        if i is textoNuevo[-1]:
                            j.write(i)
                        else:
                            j.write(f"{i}\n")
                print("Proceso realizado con éxito")
            else: 
                print("El índice no fue correcto, intente mas tarde.")
    
    def generarGestorCambios(self):
        # Generar archivo gestion cambios 
        archivo = open("Practica1/archivosSistema/solicitudes.txt", "r")
        texto = archivo.read().split("\n")

        # Discriminar por aceptar
        nuevaLista = []
        for i in texto:
            temp = i.split(" ")
            if "aceptar" in temp:
                nuevaLista.append(i)
        archivo.close()

        # Formato para gestor cambio -------------------------
        for e in nuevaLista:
            temp = e.split(" ")
            indi = nuevaLista.index(e)
            if len(temp)>13:
                temp.pop(0)
                temp.pop(1)
                temp.pop(2)
                temp.pop(2)
                temp.pop(2)
                temp.pop(2)
                temp.pop(3)
                concatenar = ""
                for j in temp:
                    if j is not temp[-1]:
                        concatenar+=f"{j} "
                    else:
                        concatenar+=f"{j}"
                nuevaLista[indi] = concatenar
            else:
                temp.pop(0)
                temp.pop(2)
                temp.pop(3)
                concatenar = ""
                for j in temp:
                    if j is not temp[-1]:
                        concatenar+=f"{j} "
                    else:
                        concatenar+=f"{j}"
                nuevaLista[indi] = concatenar

        with open("Practica1/archivos/Control_de_cambios.txt", "w") as archiv:
            # Escribir en el gestor de cambios
            for i in nuevaLista:
                if i == nuevaLista[-1]:
                    archiv.write(i)
                else:
                    archiv.write(i+"\n")
    
    def generarInventario(self):
        with open("Practica1/archivosSistema/inventarioCentroDeInvestigacion.txt", "r") as archimonde:
            texto = archimonde.read().split("\n")

            with open("Practica1/archivos/InventarioGeneral.txt", "w") as archiv:
            # Escribir en el gestor de cambios
                for i in texto:
                    if i == texto[-1]:
                        archiv.write(i)
                    else:
                        archiv.write(i+"\n")

    def consultarGestorCambios(self):
        # Generar archivo gestion cambios 
        archivo = open("Practica1/archivosSistema/solicitudes.txt", "r")
        texto = archivo.read().split("\n")

        # Discriminar por aceptar
        nuevaLista = []
        for i in texto:
            temp = i.split(" ")
            if "aceptar" in temp:
                nuevaLista.append(i)
        archivo.close()

        # Formato para gestor cambio -------------------------
        for e in nuevaLista:
            temp = e.split(" ")
            indi = nuevaLista.index(e)
            if len(temp)>13:
                temp.pop(0)
                temp.pop(1)
                temp.pop(2)
                temp.pop(2)
                temp.pop(2)
                temp.pop(2)
                temp.pop(3)
                concatenar = ""
                for j in temp:
                    if j is not temp[-1]:
                        concatenar+=f"{j} "
                    else:
                        concatenar+=f"{j}"
                nuevaLista[indi] = concatenar
            else:
                temp.pop(0)
                temp.pop(2)
                temp.pop(3)
                concatenar = ""
                for j in temp:
                    if j is not temp[-1]:
                        concatenar+=f"{j} "
                    else:
                        concatenar+=f"{j}"
                nuevaLista[indi] = concatenar

        # imprimir por pantallla 
        print("\n________________________________________________________________________________________________________________________\n")
        for i in nuevaLista:
            print(i)
        print("________________________________________________________________________________________________________________________")
