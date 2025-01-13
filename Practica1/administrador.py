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
                        if i is textoNuevo[-1]:
                            j.write(i)
                        else:
                            j.write(f"{i}\n")
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

        nuevaLista = []
        for i in texto:
            temp = i.split(" ")
            if "aceptar" in temp:
                nuevaLista.append(i)
        archivo.close()

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