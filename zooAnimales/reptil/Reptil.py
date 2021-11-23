from zooAnimales.animal import Animal
class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre)
        super().__init__(edad)
        super().__init__(habitat)
        super().__init__(genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola

    #getter y setter

    def getColorEscamas(self):
        return self._colorEscamas

    def getLargoCola(self):
        return self._largoCola


    #fin getter y setter


    def movimiento(self):
        return "reptar"

    def crearIguanas(self, nombre, edad, genero):
        self.iguanas = self.iguanas + 1
        colorEscamas = "verde"
        largoCola = 3
        habitat = "humedal"
        iguana = Reptil(nombre, edad,habitat,genero,colorEscamas,largoCola)
        self.listado.append(iguana)
        return iguana

    def crearSerpiente(self, nombre, edad, genero):
        self.serpientes = self.serpientes + 1
        colorEscamas = "blanco"
        largoCola = 1
        habitat = "jungla"
        serpiente = Reptil(nombre, edad,habitat,genero,colorEscamas,largoCola)
        self.listado.append(serpiente)
        return serpiente




