from zooAnimales.animal import Animal
class Anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre)
        super().__init__(edad)
        super().__init__(habitat)
        super().__init__(genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        self.listado.append(self)


        #getter y setter


    def getColorPiel(self):
        return self._colorPiel

    def isVenenoso(self):
        return self._venenoso



        #fin getter y setter

    def movimiento(self):
        return "saltar"

    def crearRana(self, nombre, edad, genero):
        self.ranas = self.ranas + 1

        colorPiel = "rojo"
        venenoso = True
        habitat = "selva"
        rana = Anfibio(nombre, edad,habitat,genero, colorPiel, venenoso)
        self.listado.append(rana)
        return rana

    def crearSalamandra(self, nombre, edad, genero):
        self.salamandras = self.salamandras + 1
        colorPiel = "negro y amarillo"
        venenoso = False
        habitat = "selva"

        salamandra = Anfibio(nombre, edad, habitat, genero, colorPiel, venenoso)
        self.listado.append(salamandra)
        return salamandra



