from gestion.zoologico import Zoologico
class Zona:
    animales = []
    def __init__(self, nombre, zoo):
        self._nombre = nombre
        self._zoo = zoo

    #getter y setter






    #fin getter y setter


    def agregarAnimales(self, animal):
        self.animales.append(animal)

    def cantidadAnimales(self):
        return len(self.animales)