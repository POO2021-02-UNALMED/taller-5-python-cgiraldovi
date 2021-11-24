from gestion.zoologico import Zoologico
class zona:
    animales = []
    def __init__(self, nombre, zoo = None):
        self._nombre = nombre
        self._zoo = zoo

    #getter y setter

    def getNombre(self):
        return self._nombre

    def getZoo(self):
        return self._zoo


    #fin getter y setter


    def agregarAnimales(self, animal):
        self.animales.append(animal)

    def cantidadAnimales(self):
        return len(self.animales)