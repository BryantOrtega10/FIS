from app.objetos_sesion.Producto import Producto

class Entrada(Producto):
    
    def __init__(self, idProducto, nombre, precio, foto, ingredientes, ingredientesSeleccionados, adiciones, adicionesSeleccionadas, maxIngBase, aplicaMax, minIngBase, aplicaMin):
        super().__init__(idProducto, nombre, precio, foto, 0, ingredientes, ingredientesSeleccionados, adiciones, adicionesSeleccionadas, maxIngBase, aplicaMax, minIngBase, aplicaMin)



