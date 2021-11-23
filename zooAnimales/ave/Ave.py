from zooAnimales.animal import Animal
class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre)
        super().__init__(edad)
        super().__init__(habitat)
        super().__init__(genero)
        self._colorPlumas = colorPlumas
        self.listado.append(self)




        #getter y setter

    def getColorPlumas(self):
        return self._colorPlumas

        #fin getter y setter



    def movimiento(self):
        return "volar"

    def crearHalcon(self, nombre, edad, genero):
        self.halcones = self.halcones + 1
        colorPlumas = "cafe glorioso"
        habitat = "montanas"
        halcon = Ave(nombre,edad,habitat,genero,colorPlumas)
        self.listado.append(halcon)
        return halcon

    def crearAguila(self, nombre, edad, genero):
        self.aguilas = self.aguilas + 1
        colorPlumas = "blanco y amarillo"
        habitat = "montanas"
        aguila = Ave(nombre,edad,habitat,genero,colorPlumas)
        self.listado.append(aguila)
        return aguila





