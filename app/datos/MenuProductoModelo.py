from app.datos.MysqlConnector import MysqlConnection


class MenuProductoModelo:
    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, id_menu, id_producto):
        if id_menu == '':
            return {'success': False, 'error': "Id de menu  vacio"}
        if id_producto == '':
            return {'success': False, 'error': "Id de producto vacio"}

        res = self.__conector.insert("menu_producto", {"fk_menu": id_menu,
                                                            "fk_producto": id_producto})
        if res['success'] == True:
            self.__conector.commit()

        return res

    def obtenerFKProductos(self, id_menu):
        if id_menu != '':
            return self.__conector.select(fields=['fk_producto','tipo'],
                                          tables=['menu_producto','producto'],
                                          where='menu_producto.fk_producto = producto.id_producto and fk_menu=%(id_menu)s',
                                          values={'id_menu': id_menu})
        else:
            return {'success': False, 'error': "Id de menu vacio"}

    def eliminarPorMenu(self, id_menu):
        res = self.__conector.delete(table='menu_producto',
                                     where='fk_menu=%(id_menu)s',
                                     values={'id_menu': id_menu})
        if res['success']:
            self.__conector.commit()

        return res
