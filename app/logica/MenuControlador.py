import os
from app.datos.MenuModelo import MenuModelo
from werkzeug.utils import secure_filename


class MenuControlador:

    def __init__(self):
        self.__modelo = MenuModelo()
        self.__UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", 'static/uploads'))

    def lista(self):
        menus = self.__modelo.obtener()
        return menus

    def obtener_x_id(self, id):
        menu = self.__modelo.obtenerUno(id)
        return menu

    def agregar(self, request):
        foto = ''
        if 'foto' in request.files:
            file = request.files['foto']
            if file.filename != '':
                foto = secure_filename(file.filename)
                file.save(os.path.join(self.__UPLOAD_FOLDER, foto))

        res = self.__modelo.agregar(request.form.get('nombre'), foto, request.form.get('precio'), request.form.get('id_restaurante'))
        return res

    def modificar(self, id, request):
        menu = self.__modelo.obtenerUno(id)
        menu = menu[0]

        foto = menu["foto"]
        if 'foto' in request.files:
            file = request.files['foto']
            if file.filename != '':
                os.remove(self.__UPLOAD_FOLDER + "/" + foto)
                foto = secure_filename(file.filename)
                file.save(os.path.join(self.__UPLOAD_FOLDER, foto))

        res = self.__modelo.modificar(id, request.form.get('nombre'), foto, request.form.get('und_medida'), request.form.get('id_restaurante'))
        return res

    def eliminar(self, id):
        res = self.__modelo.eliminar(id)
        return res