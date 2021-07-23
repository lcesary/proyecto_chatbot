from tornado.gen import coroutine
from .managers import *
from ..usuarios.managers import *
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError
from ..common.controllers import CrudController, SuperController, ApiController
from xhtml2pdf import pisa
import os.path

class Report:
    def html_to_pdf(self, sourceHtml, nombre):
        outputFilename = 'server/common/resources/downloads/' + nombre

        resultFile = open(outputFilename, "w+b")
        pisaStatus = pisa.CreatePDF(
            sourceHtml,
            dest=resultFile)
        resultFile.close()

        return pisaStatus.err

global report
report = Report()
global image_report
image_report = "server/common/resources/images/pst.jpg"

class UbicacionController(CrudController):

    manager = UbicacionManager
    html_index = "rastreo/views/ubicacion/index.html"
    html_table = "rastreo/views/ubicacion/table.html"
    routes = {
        '/ubicacion': {'GET': 'index', 'POST': 'table'},
        '/insert_ubicacion': {'POST': 'insert_ubicacion'},
    }

    def insert_ubicacion(self):
        self.set_session()
        ins_manager = self.manager(self.db)
        diccionary = json.loads(self.get_argument("object"))
        diccionary['fkpersona'] = self.get_user_id()
        object = ins_manager.entity(**diccionary)
        indicted_object = ins_manager.insert(object)
        if len(ins_manager.errors) == 0:
            self.respond(indicted_object.get_dict(), message='Insertado correctamente!')
        else:
            self.respond([item.__dict__ for item in ins_manager.errors], False, 'Ocurrió un error al insertar')
        self.db.close()

    def get_extra_data(self):
        aux = super().get_extra_data()
        aux['latitud'] = UbicacionManager(self.db).obtener()
        return aux

    def consultar_ubicacion(self):
        self.set_session()
        result = self.manager(self.db).obtener()



    def index(self):
        self.set_session()
        self.verif_privileges()
        result = self.manager(self.db).list_all()
        result['privileges'] = UsuarioManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
        result.update(self.get_extra_data())
        self.render(self.html_index, **result)
        self.db.close()