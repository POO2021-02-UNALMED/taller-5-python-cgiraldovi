from zooAnimales.animal import Animal
class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre)
        super().__init__(edad)
        super().__init__(habitat)
        super().__init__(genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        self.listado.append(self)




        #getter y setter






        #fin getter y setter



    def movimiento(self):
        return "nadar"

    def crearSalmon(self, nombre, edad, genero):
        self.salmones = self.salmones + 1
        colorEscamas = "rojo"
        cantidadAletas = 6
        habitat = "oceano"
        salmon = Pez(nombre,edad,habitat,genero,colorEscamas,cantidadAletas)
        self.listado.append(salmon)
        return salmon


    def crearBacalao(self, nombre, edad, genero):
        self.bacalaos = self.bacalaos + 1
        colorEscamas = "gris"
        cantidadAletas = 6
        habitat = "oceano"
        bacalao = Pez(nombre,edad,habitat,genero,colorEscamas,cantidadAletas)
        self.listado.append(bacalao)
        return bacalao