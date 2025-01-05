class Sistema:
    
    def __init__(self, empleados=None, equipos=None):
        self._empleados = empleados
        self._equipos = equipos


if __name__ == "__main__":

    archivoEmpleados = open("Practica1/archivos/Empleados.txt","r")
    while True:
        usuario = archivo.readline()
        usuario = usuario.strip()
        if not usuario:
            break
        else:
            nombre,id,fecha_nacimiento,ciudad_nacimiento,tel,email,dir = usuario.split("/")
            dia, mes, año = fecha_nacimiento.split("-")
            ciudad,calle,nomenclatura,barrio,edificio,apto = dir.split(" ")  
            usuario1 = Usuario(nombre,id,Fecha(int(dia),int(mes),int(año)),ciudad_nacimiento,tel,email,Direccion(calle,ciudad,nomenclatura,barrio,edificio,apto))
            ordenador.agregarUsuario(usuario1)

    archivo.close()
    