from tornado.gen import coroutine
from .managers import *
from ..usuarios.managers import *
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError
from ..common.controllers import CrudController, SuperController, ApiController
from xhtml2pdf import pisa
import os.path

class PagoController(CrudController):

    manager = PagoManager
    html_index = "ubicacion/views/ubicacion/index.html"
    html_table = "ubicacion/views/ubicacion/table.html"
    routes = {
        '/ubicacion': {'GET': 'index', 'POST': 'table'}
    }