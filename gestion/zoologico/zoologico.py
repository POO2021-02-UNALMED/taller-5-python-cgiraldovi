from gestion.zona import Zona
class zoologico:
    zonas = []

    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self.ubicacion = ubicacion


    #getter y setter

    def getNombre(self):
        return self._nombre

    def getZona(cls):
        return cls.zonas


    #fin getter y setter

    def agregarZonas(cls, zona):
        cls.zonas.append(zona)

    def cantidadTotalAnimales(self):
        contador = 0
        for zona in self.zonas:
            contador += zona.cantidadAnimales()
        return contador