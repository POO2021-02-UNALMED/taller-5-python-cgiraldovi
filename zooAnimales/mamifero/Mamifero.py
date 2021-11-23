from zooAnimales.animal import Animal
class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        self.listado.append(self)

        #getter y setter

    def isPelaje(self):
        return self._pelaje

    def getPatas(self):
        return self._patas

        #fin getter y setter



    def crearCaballo(self, nombre, edad, genero):
        self.caballos = self.caballos + 1
        pelaje = True
        patas = 4
        habitat = "pradera"
        caballo = Mamifero(nombre, edad, habitat, genero, pelaje, patas)
        self.listado.append(caballo)
        return caballo

    def crearLeon(self, nombre, edad, genero):
        self.leones = self.leones + 1
        pelaje = True
        patas = 4
        habitat = "selva"
        leon = Mamifero(nombre, edad, habitat, genero, pelaje, patas)
        self.listado.append(leon)
        return leon



