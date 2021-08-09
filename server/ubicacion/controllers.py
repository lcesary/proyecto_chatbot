from tornado.gen import coroutine
from .managers import *
from ..usuarios.managers import *
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError
from ..common.controllers import CrudController, SuperController, ApiController
from xhtml2pdf import pisa
import os.path

class UbicacionController(CrudController):

    manager = UbicacionManager
    html_index = "ubicacion/views/ubicacion/index.html"
    html_table = "ubicacion/views/ubicacion/table.html"
    routes = {
        '/ubicacion': {'GET': 'index', 'POST': 'table'}
    }


class CarreraController(CrudController):

    manager = CarreraManager
    html_index = "ubicacion/views/carrera/index.html"
    html_table = "ubicacion/views/carrera/table.html"
    routes = {
        '/carrera': {'GET': 'index', 'POST': 'table'}
    }

    def index(self):
        self.set_session()
        self.verif_privileges()
        result = self.manager(self.db).list_all()
        result['privileges'] = UsuarioManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
        result.update(self.get_extra_data())
        self.render(self.html_index, **result)
        self.db.close()