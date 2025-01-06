class Investigador(Usuario):

    def __init__(self):
        self._equipos = []

    def agregarEquipo(self, equipo):
        self._equipos.append(equipo)
    pass