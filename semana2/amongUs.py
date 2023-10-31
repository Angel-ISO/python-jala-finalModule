import random

class CodingAmongUs:
    def __init__(self):
        pass

class Jugador:
    def __init__(self, color, accesorios):
        self.rol = "tripulante"
        self.color = color
        self.accesorios = accesorios

class Tripulantes:
    def __init__(self):
        self.tripulantes = []
        self.determinar_rol()

    def agregar_tripulante(self, name, color, accesorios):
        self.tripulantes.append(Jugador(name ,color, accesorios))

    def determinar_rol(self):
        seleccionado = random.choice(self.tripulantes)
        seleccionado.rol = "Impostor"
        return seleccionado

tripulantes = Tripulantes()
tripulantes.agregar_tripulante("jugador 1", "Rojo", ["Sombrero"])
tripulantes.agregar_tripulante("jugador 2", "Rojo", ["Sombrero"])
tripulantes.agregar_tripulante("jugador 3", "Rojo", ["Sombrero"])
tripulantes.agregar_tripulante("jugador 4", "Rojo", ["Sombrero"])
tripulantes.agregar_tripulante("jugador 5", "Rojo", ["Sombrero"])
tripulantes.agregar_tripulante("jugador 6", "Rojo", ["Sombrero"])
