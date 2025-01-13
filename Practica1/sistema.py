from direccion import Direccion
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

    def accesoSistema(self, cedula, contraseña):
        archivoPassword = open("Practica1/archivosSistema/Password.txt","r")
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
        indice = self.busqueda(cedula, "empleado-ID")
        empleado = indice.getData()

        while True:
            print("\nQue proceso desea realizar:")
            print("1. Consultar mis equipos.")
            print("2. Registrar usuarios.")
            print("3. Eliminar usuarios.")
            print("4. cambiar contraseñas.")
            print("5. Generar txt de inventario de empleado")
            print("6. Atender solicitudes.")
            print("7. generar txt con solicitudes.")
            print("8. generar txt de control de cambios")
            print("9. generar txt con inventario general.")
            print("10. Salir.")
            indice = int(input("Ingrese un indice: "))

            if indice == 1: # Consulta equipos -----------------------------------------------------------------------
                empleado.consultaEquipos()
                indice12 = input("Desea realizar otra accion si/no:")
                if indice12 == "si":
                    pass
                elif indice12 == "no":
                    break
            
            elif indice == 2: # Registro usuario -------------------------------------------------------------------
                print("Ingrese los datos para registrar al nuevo usuario: ")
                # Pedimos todos los datos necesarios -----------------------------------
                rol =  input("Rol del nuevo usuario: (investigador o administrador): ")
                datosUsuario = input("Nombre, cedula, ciudad de nacimiento, telefono e email separados por espacios: ")
                nombre, cedu, ciudad_na, tel, email = datosUsuario.split(" ")

                fecha_na  = input("Fecha de nacimiento separada por (-): ") 
                dia, mes, anio = fecha_na.split("-")
                fecha = Fecha(int(dia), int(mes) ,int(anio))

                Direccioon = input("Dirección separada por espacios (Calle, ciudad, nomenclatura, barrio, edificio, apto) en caso de no contar con los ultimos dos coloque None:\n")
                calle, ciudad, nomenclatura, barrio, edificio, apto = Direccioon.split(" ")
                if (edificio and apto == "None") or  (edificio and apto == "none"):
                    edificio = None 
                    apto = None
                dir = Direccion(calle, ciudad, nomenclatura, barrio, edificio, apto)

                contrasenia = input("Ingrese una contraseña para el usuario: ")
                # Creamos el usuario------------------------------------------------
                if rol == "administrador" or "Administrador":
                    usuNuevo = Administrador(nombre, int(cedu), fecha,ciudad_na, int(tel), email, dir)

                    contras = open("Practica1/archivosSistema/password.txt", "r+")
                    contras.read()
                    contras.write(f"\n{cedu} {contrasenia} {rol}")
                    contras.close()

                    self._empleados.addLast(usuNuevo)
                    self.ordenar("empleados")

                elif rol == "investigador" or "Investigador":
                    usuNuevo = Investigador(nombre, int(cedu), fecha,ciudad_na, int(tel), email, dir)

                    contras = open("Practica1/archivosSistema/password.txt", "r+")
                    contras.read()
                    contras.write(f"\n{cedu} {contrasenia} {rol}")
                    contras.close()

                    self._empleados.addLast(usuNuevo)
                    self.ordenar("empleados")

                else:
                    print("Error en la elección del rol del usuario")
                    pass

            elif indice == 3: # Eliminación usuario ------------------------------------------------
                cedu = int(input("ingrese el documento del usuario que quiera eliminar: "))
                busqueda = self.busqueda(cedu, "empleado-ID")
                if busqueda is not None:
                    usuEliminar = busqueda.getData()
                    print(usuEliminar)

                    # Eliminar contraseña ---------------------------------------------
                    with open("Practica1/archivosSistema/Password.txt", "r") as archivo:
                        # Leemos el contenido y procesamos
                        texto = archivo.read().replace("\n", " ")
                        texto2 = texto.split(" ")

                    cedula = usuEliminar.getId() # Cedula a eliminar
                    if str(cedula) in texto2:
                        indice = texto2.index(str(cedula))
                        contra = texto2[indice + 1]
                        rol = texto2[indice + 2]
                        print(contra, rol)    
                        # Eliminamos la cédula, la contraseña y el rol
                        texto2.pop(indice + 2)  # Rol
                        texto2.pop(indice + 1)  # Contraseña
                        texto2.pop(indice)      # Cedula
                    # Reescribimos el documento contraseña ---------------------------
                    with open("Practica1/archivosSistema/Password.txt", "w") as archivo:
                        contador = 0
                        for i in texto2:
                            contador += 1
                            if contador != 3:
                                archivo.write(i + " ")
                            else:
                                if i is not texto2[-1]:
                                    archivo.write(i + "\n")
                                    contador = 0
                                else:
                                    archivo.write(i)
                                    contador = 0

                    # Eliminamos su registro en la lista de empleados -----------------
                    with open("Practica1/archivosSistema/Empleados.txt", "r") as archivo:
                        # Leemos el contenido y procesamos
                        texto = archivo.read().split("\n")

                    Usuario = usuEliminar.__str__()
                    # Verificamos si la cédula está en el contenido
                    if Usuario in texto:
                        print("Se ha eliminado correctamente")
                        texto.remove(Usuario)

                    with open("Practica1/archivosSistema/Empleados.txt", "w") as archivo:
                        for i in texto:
                            if i is not texto[-1]:
                                archivo.write(i + "\n")
                            else:
                                archivo.write(i)
                    
                    # Eliminamos el Nodo del empleado y el texto de inventario: 
                    temp = self._empleados._head
                    while temp.getData()!=usuEliminar:
                        prev = temp
                        temp = temp.getNext()
                    if temp == self._empleados._head:
                        self._empleados._head = temp.getNext()
                        temp.setNext(None)
                    else:
                        apuntador = temp.getNext()
                        prev.setNext(apuntador)
                        temp.setNext(None)

                    # Eliminar del inventario general ---------------------------------------------
                    with open("Practica1/archivosSistema/inventarioCentroDeInvestigacion.txt", "r") as archivo:
                        # Leemos el contenido y procesamos
                        texto = archivo.read().split("\n")

                        nombre = usuEliminar.getNombre()
                        # Guardamos en textoNuevo el inventario actualizado
                        textoNuevo = []
                        for i in texto:
                            temp = i.split(" ")
                            if nombre not in temp:
                                textoNuevo.append(i)
                                
                    # Reescribimos 
                    with open("Practica1/archivosSistema/inventarioCentroDeInvestigacion.txt", "w") as archivo:
                        contador = 1
                        for i in textoNuevo:
                            if contador != len(textoNuevo):
                                archivo.write(f"{i}\n")
                            else:
                                archivo.write(i)
                            contador+=1

                else:
                    print("No se encontró el usuario a eliminar")

            elif indice == 4:
                # Cambiar contraseña ---------------------------------------------
                print("Ingrese la cédula del usuario al que le va a cambiar la contraseña: ")
                ceduCambio = input()

                with open("Practica1/archivosSistema/Password.txt", "r") as archivo:
                    # Leemos el contenido y procesamos
                    texto = archivo.read().split("\n")
                    
                    captura = ""
                    indiceText = 0
                    for i in texto:
                        temp = i.split(" ")
                        if ceduCambio in temp:
                            indice = temp.index(ceduCambio)
                            rol = temp[indice+2]
                            nuevaContra = input("Ingrese la nueva contraseña: ")
                            indiceText = texto.index(i)
                            texto[indiceText] = f"{ceduCambio} {nuevaContra} {rol}"
                # Reescribimos 
                with open("Practica1/archivosSistema/Password.txt", "w") as archivo:
                    contador = 1
                    for i in texto:
                        if contador != len(texto):
                            archivo.write(f"{i}\n")
                        else:
                            archivo.write(i)
                        contador+=1

            elif indice == 5:
                cc = int(input("Ingrese el Id del empleado para generar el txt: "))
                nodo = self.busqueda(cc, "empleado-ID")
                if nodo != None:
                    encontrado = nodo.getData()
                    empleado.generarDocInventario(encontrado)
                    print("Operación realizada con exito.")
                else: 
                    print("Cedula incorrecta, vuelva a intentarlo")

            elif indice == 6:
                # Atender solicitudes
                # leer solicitudes en Control de cambio
                control = open("Practica1/archivosSistema/solicitudes.txt", "r") 
                texto = control.read().split("\n")
                indu = int(input("¿Qué categoría desea ver? (1. eliminar 2. agregar) equipos: "))

                if indu==2: # Agregar equipo ---------------------------------------------------------
                    contador = 1
                    for i in texto:
                        separado = i.split(" ")
                        if "agregar" in separado and "pendiente" in separado:
                            print(f"{contador}. {i}")
                        contador+=1

                    indice = int(input("Selecione la solicitud que desea revisar: "))
                    indice = indice-1
                    comparador = texto[indice].split(" ")
                    if "pendiente" not in comparador:
                        print("La solicitud ya fue contestada.")
                    else: 
                        respuesta = int(input("Desea 1. rechazar o 2. aceptar, indique el número de su respuesta: "))
                        if respuesta == 1: 
                            nuevo = texto[indice].split(" ")
                            nuevo[-1] = "rechazar"
                            print("operación realizada con éxito")
                            concatenar = ""
                            for i in nuevo:
                                if i is not nuevo[-1]:
                                    concatenar+=i+" "
                                else:
                                    concatenar+=i
                            texto[indice] = concatenar
                        elif respuesta == 2:
                            nuevo = texto[indice].split(" ")
                            nuevo[-1] = "aceptar"
                            print("operación realizada con éxito, inventario general actualizado.")
                            concatenar = ""
                            for i in nuevo:
                                if i is not nuevo[-1]:
                                    concatenar+=i+" "
                                else:
                                    concatenar+=i
                            texto[indice] = concatenar
                            
                            # Actualizar inventario general
                            idEmpleado,nombre,codigo,dia,mes,año,valor = nuevo[1:8]
                            empleado12 = self.busqueda(idEmpleado,"empleado-ID")
                            self._equipos.addFirst(Equipo(nombre,codigo,Fecha(int(dia),int(mes),int(año)),valor,empleado12.getData()))
                            self.ordenar("equipos")

                                # Recojemos la lista
                        else: 
                            print("índice no válido")
                        with open("Practica1/archivosSistema/solicitudes.txt", "w") as j:
                            for i in texto:
                                if i is not texto[-1]:
                                    j.write(f"{i}\n")
                                else:
                                    j.write(f"{i}")

                elif indu==1: # Eliminar equipo --------------------------------------------
                    contador = 1
                    for i in texto:
                        separado = i.split(" ")
                        if "eliminar" in separado and "pendiente" in separado:
                            print(f"{contador}. {i}")
                        contador+=1

                    soli = int(input("Seleccione la solicitud que desea atender: "))
                    soli-=1
                    serieEquipo = texto[soli].split(" ")

                    deseo = int(input("Desea (1. aceptar o 2. rechazar la solicitud): "))
                    serie = int(serieEquipo[2])

                    if deseo == 1: # Acpetar eliminar -----------------------------------------
                        serie = int(serieEquipo[2])
                        # recorrer lista equipos 
                        print(serie)
                        temp = self._equipos.first()
                        while True:
                            if int(temp.getData().getNoPlaca()) == int(serie):
                                break
                            elif temp == None:
                                break
                            temp = temp.getNext()

                        if temp!=None:
                            self._equipos.remove(temp.getData())
                            # Ordenamos una vez se elimina ----------------------------------------------

                            buscar = open("Practica1/archivosSistema/inventarioCentroDeInvestigacion.txt", "r")
                            tex = buscar.read().split("\n")
                            for i in tex:
                                separao = i.split(" ")
                                if int(separao[3]) == int(serie):
                                    tex.remove(i)
                            buscar.close()
                            with open("Practica1/archivosSistema/inventarioCentroDeInvestigacion.txt", "w") as ree:
                                for i in tex:
                                    if i == tex[-1]:
                                        ree.write(i)  
                                    else:
                                        ree.write(i+"\n")

                            print("Se ha eliminado correctamente")
                            comprobante = False
                            for i in texto:
                                temp = i.split(" ")
                                if "eliminar" in temp:
                                    if int(temp[2]) == serie:
                                        posicion = texto.index(i)
                                        temp.remove("pendiente")
                                        temp.append("aceptar")

                                        concatenar = ""
                                        for e in temp:
                                            if e is temp[-1]:
                                                concatenar+=e
                                            else:
                                                concatenar+=e+" "
                                        comprobante = True 
                                        texto[posicion] = concatenar
                            if comprobante:# Actualizar lista solis
                                print("Se ha actualizado la lista de solicitudes")
                                with open("Practica1/archivosSistema/solicitudes.txt","w")as h:
                                    for i in texto:
                                        if i is not texto[-1]:
                                            h.write(i+"\n")
                                        else:
                                            h.write(i)
                        else: 
                            print("No fue posible eliminar el equipo")

                    else: # Rechazar eliminar -------------------------------------------------
                        comprobante = False
                        for i in texto:
                            temp = i.split(" ")
                            if "eliminar" in temp:
                                if int(temp[2]) == serie:
                                    posicion = texto.index(i)
                                    temp.remove("pendiente")
                                    temp.append("rechazar")

                                    concatenar = ""
                                    for e in temp:
                                        if e is temp[-1]:
                                            concatenar+=e
                                        else:
                                            concatenar+=e+" "
                                    comprobante = True 
                                    texto[posicion] = concatenar
                        if comprobante:# Actualizar lista solis
                            print("Se ha actualizado la lista de solicitudes")
                            with open("Practica1/archivosSistema/solicitudes.txt","w")as h:
                                for i in texto:
                                    if i is not texto[-1]:
                                        h.write(i+"\n")
                                    else:
                                        h.write(i)
                        else:
                            print("No fue posible encontrar esa solicitud, quizá ya fue contestada") 
                else:
                    print("Indice inválido")

            elif indice == 7: # generar txt solicitudes pendientes -----------------------------------------
                opcion = int(input("Desea ver solicitudes pendientes (1. agregar o 2. eliminar)?: "))
                empleado.generarDocSolicitudes(opcion)
            elif indice == 8: # generar txt gestion de cambios -------------------------------------------
                print("Se he generado correctamente un doc con la gestion de los cambios")
                empleado.generarGestorCambios()
            elif indice==9: # Generar txt gestor de cambios
                print("Se ha generado correctamente un doc con el inventario general")
                empleado.generarInventario()
            elif indice==10: # Salir del bucle
                break
            else: 
                print("Indice no válido")
        # ------------------------------------------
    def accesoInvestigador(self, cedula):
        empleado = self.busqueda(cedula,"empleado-ID")
        while True:
            print("Que proceso desea realizar:")
            print("1.Consultar mis equipos.")
            print("2.Adicionar equipo.")
            print("3.Eliminar equipo.")
            print("4.Consulta estado solicitudes.")
            print("5.Generar archivo inventario.")
            print("6.Generar archivo solicitudes.")
            print("7.Salir.")
            indice = int(input("Ingrese un indice:"))
            if indice == 1:
                empleado.getData().consultaEquipos()
                indice12 = input("Desea realizar otra accion si/no: ")
                if indice12 == "si":
                    pass
                elif indice12 == "no":
                    break
            elif indice == 2:
                empleado.getData().adicionarEquipo()
                indice12 = input("Desea realizar otra accion si/no: ")
                if indice12 == "si":
                    pass
                elif indice12 == "no":
                    break

            elif indice == 3:
                empleado.getData().eliminarEquipo()
                indice12 = input("Desea realizar otra accion si/no: ")
                if indice12 == "si":
                    pass
                elif indice12 == "no":
                    break

            elif indice == 4: 
                empleado.getData().consultaEstadoSolicitudes()
                indice12 = input("Desea realizar otra accion si/no: ")
                if indice12 == "si":
                    pass
                elif indice12 == "no":
                    break
            
            elif indice == 5:
                empleado.getData().archivoInventario()
                indice12 = input("Desea realizar otra accion si/no: ")
                if indice12 == "si":
                    pass
                elif indice12 == "no":
                    break

            elif indice == 6:
                empleado.getData().archivoSolicitudes()
                indice12 = input("Desea realizar otra accion si/no: ")
                if indice12 == "si":
                    pass
                elif indice12 == "no":
                    break

            elif indice == 7:
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
            while(temp != None and int(temp.getData().getId()) != int(dato)):
                temp = temp.getNext()
            return temp

    def ordenar(self,tipo):
        if "equipos" == tipo:
            nodo = self._equipos.first()
            while nodo:
                nodo2 = nodo.getNext()
                while nodo2:
                    if nodo.getData().getNoPlaca() > nodo2.getData().getNoPlaca():
                        self.intercambiar(nodo,nodo2)
                    nodo2 = nodo2.getNext()
                nodo = nodo.getNext()
            
            archivo = open("Practica1/archivosSistema/inventarioCentroDeInvestigacion.txt","w")
            temporal = sistema._equipos.first()
            while temporal != None:
                archivo.write(f"{temporal.getData().getEmpleado().getNombre()} {temporal.getData().getEmpleado().getId()} {temporal.getData()}\n")
                temporal = temporal.getNext()
            archivo.close()
        
        elif "empleados" == tipo:
            nodo = self._empleados.first()
            while nodo:
                nodo2 = nodo.getNext()
                while nodo2:
                    if nodo.getData().getId() > nodo2.getData().getId():
                        self.intercambiar(nodo,nodo2)
                    nodo2 = nodo2.getNext()
                nodo = nodo.getNext()
            
            archivo = open("Practica1/archivosSistema/empleados.txt","w")
            temporal = sistema._empleados.first()
            while temporal != None:
                archivo.write(f"{temporal.getData()}\n")
                temporal = temporal.getNext()
            archivo.close()
            
            

    def intercambiar(self,primero,segundo):
        temporal = primero.getData()
        primero.setData(segundo.getData())
        segundo.setData(temporal)

        




if __name__ == "__main__":

    sistema = Sistema()

    archivoEmpleados = open("Practica1/archivosSistema/Empleados.txt","r")
    while True:
        usuario = archivoEmpleados.readline()
        usuario = usuario.strip()
        if not usuario:
            break
        else:
            nombre,id,fecha_nacimiento,ciudad_nacimiento,tel,email,dir = usuario.split("/")
            dia, mes, año = fecha_nacimiento.split("-")
            ciudad,calle,nomenclatura,barrio,edificio,apto = dir.split(" ")  
            
            archivoPassword = open("Practica1/archivosSistema/Password.txt","r")
            
            while True:
                descripcion = archivoPassword.readline()
                descripcion = descripcion.strip()
                if not descripcion:
                    archivoPassword.close()
                    break
                else:
                    cedulaP,contraseñaP,descripcion1 = descripcion.split(" ")
                    if id == cedulaP:
                        if descripcion1 == "administrador":
                            usuario1 = Administrador(nombre,id,Fecha(int(dia),int(mes),int(año)),ciudad_nacimiento,tel,email,Direccion(calle,ciudad,nomenclatura,barrio,edificio,apto))
                            sistema._empleados.addLast(usuario1)
                        
                        elif descripcion1 == "investigador":
                            usuario1 = Investigador(nombre,id,Fecha(int(dia),int(mes),int(año)),ciudad_nacimiento,tel,email,Direccion(calle,ciudad,nomenclatura,barrio,edificio,apto))
                            sistema._empleados.addLast(usuario1)
                


    archivoEquipos = open("Practica1/archivosSistema/inventarioCentroDeInvestigacion.txt","r")
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
            sistema._equipos.addLast(equipo1)


    archivoEquipos.close()


    cedula = int(input("Ingrese su documento: "))
    contraseña = input("Ingrese su contraseña: ")
    sistema.accesoSistema(cedula,contraseña)



