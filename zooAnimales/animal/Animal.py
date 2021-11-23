class Animal:
    totalAnimales = 0
    totalMamiferos = 0
    totalAves = 0
    totalReptiles = 0
    totalPeces = 0
    totalAnfibios = 0


    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self.totalAnimales = self.totalAnimales + 1



        #getter y setter






        #fin getter y setter

    def movimiento(self):
        return "desplazarse"


    def totalPorTipo(self):
        return "hola"

    def toString(self):
        return "hola"
