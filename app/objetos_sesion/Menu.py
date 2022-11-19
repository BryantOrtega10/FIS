from app.logica.MenuControlador import MenuControlador

class Menu:

    def __init__(self, idMenu="", nombre="", foto="", precio="", estado="", entrada=None, bebida=None, postre=None, platoFuerte=None, acompanamiento=None):
        self.__idMenu = idMenu
        self.__nombre = nombre
        self.__foto = foto
        self.__precio = precio
        self.__estado = estado
        self.__entrada = entrada
        self.__bebida = bebida
        self.__postre = postre
        self.__platoFuerte = platoFuerte
        self.__acompanamiento = acompanamiento

        self.__menuControlador = MenuControlador()

    def setBdInfoMenu(self, id):
        infoProducto = self.__menuControlador.obtener_x_id(id)
        if infoProducto:
            infoProducto = infoProducto[0]
            self.__idMenu = infoProducto["id_menu"]
            self.__nombre = infoProducto["nombre"]
            self.__foto = infoProducto["foto"]
            self.__precio = infoProducto["precio"]

    def getIdMenu(self):
        return self.__idMenu

    def setIdMenu(self, value):
        self.__idMenu = value

    def getNombre(self):
        return self.__nombre

    def setNombre(self, value):
        self.__nombre = value

    def getPrecio(self):
        return self.__precio

    def setPrecio(self, value):
        self.__precio = value

    def getFoto(self):
        return self.__foto

    def setFoto(self, value):
        self.__foto = value

    def getEstado(self):
        return self.__estado

    def setEstado(self, value):
        self.__estado = value

    def getEntrada(self):
        return self.__entrada

    def setEntrada(self, value):
        self.__entrada = value

    def getBebida(self):
        return self.__bebida

    def setBebida(self, value):
        self.__bebida = value

    def getPostre(self):
        return self.__postre

    def setPostre(self, value):
        self.__postre = value

    def getPlatoFuerte(self):
        return self.__platoFuerte

    def setPlatoFuerte(self, value):
        self.__platoFuerte = value

    def getAcompanamiento(self):
        return self.__acompanamiento

    def setAcompanamiento(self, value):
        self.__acompanamiento = value
