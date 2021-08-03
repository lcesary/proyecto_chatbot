import base64

from tornado.gen import coroutine

from .managers import *
from ..usuarios.managers import *
from ..operaciones.managers import *
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError
from ..common.controllers import CrudController, SuperController, ApiController
from xhtml2pdf import pisa
import os.path
import dropbox


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
image_report = "../server/common/resources/images/sabsa.jpg"


class PersonaController(CrudController):

    manager = PersonaManager
    html_index = "persona/views/personal/index.html"
    html_table = "persona/views/personal/table.html"
    routes = {
        '/personal': {'GET': 'index', 'POST': 'table'},
        '/personal_insert': {'POST': 'insert'},
        '/personal_update': {'PUT': 'edit', 'POST': 'update'},
        '/personal_delete': {'POST': 'delete'},
    }



    def index(self):
        self.set_session()
        self.verif_privileges()
        result = self.manager(self.db).list_all()
        result['privileges'] = UsuarioManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
        result.update(self.get_extra_data())
        for a in result['objects']:
            b = a.sexo
            if (b == '0'):
                a.sexo = "Masculino"
            else:
                a.sexo = "Femenino"

        self.render(self.html_index, **result)
        self.db.close()

    def insert(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        #if "archivo" in self.request.files:
         #   cliente = dropbox.Dropbox('cLmD-0p1dtAAAAAAAAAAHeDultc8bjzmfdHNMPOCS4h8WPXAOKYIBj395iED2Ect')

#            fileinfo = self.request.files["archivo"][0]
 #           fname = fileinfo.filename
  #          extn = os.path.splitext(fname)[1]
   #         cname = str(uuid.uuid4()) + extn
            # CORRECCION DROPBOX
    #        respuesta = cliente.files_upload(fileinfo.body, '/images/' + cname)
     #       link = cliente.sharing_create_shared_link('/images/' + cname)
      #      ruta = str(link.url).replace("dl=0", "raw=1")
       #     diccionary['foto'] = ruta
       # else:
        #    link = 'https://www.dropbox.com/s/zunssxqzvm9jnns/user.png?raw=1'
         #   diccionary['foto'] = link
        if "archivo" in self.request.files:
            fileinfo = self.request.files["archivo"][0]
            fname = fileinfo.filename
            extn = os.path.splitext(fname)[1]
            cname = str(uuid.uuid4()) + extn
            f = open("./server/common/resources/images/cliente_imagenes/" + cname, 'wb')
            f.write(fileinfo.body)
            f.close()
            diccionary['foto'] = "/resources/images/cliente_imagenes/" + cname
        objeto = self.manager(self.db).entity(**diccionary)
        PersonaManager(self.db).insert(objeto)
        if ("estudiante"!= diccionary['tipo']):
            fkpersona = self.manager(self.db).obtener_x_codigo(objeto.codigo)
            objeto= self.manager(self.db).insertarpersona(objeto,fkpersona.id)
            PersonalManager(self.db).insert(objeto)
        self.respond(success=True, message='Insertado correctamente.')

    def update(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        if "archivo" in self.request.files:
            fileinfo = self.request.files["archivo"][0]
            fname = fileinfo.filename
            extn = os.path.splitext(fname)[1]
            cname = str(uuid.uuid4()) + extn
            f = open("./server/common/resources/images/cliente_imagenes/" + cname, 'wb')
            f.write(fileinfo.body)
            f.close()
            diccionary['foto'] = "/resources/images/cliente_imagenes/" + cname
        objeto = self.manager(self.db).entity(**diccionary)
        PersonalManager(self.db).update(objeto)
        self.respond(success=True, message='Modificado correctamente.')
        self.db.close()


class PeticionController(CrudController):

    manager = PeticionManager
    html_index = "persona/views/peticion/index.html"
    html_table = "persona/views/peticion/table.html"
    routes = {
        '/peticion': {'GET': 'index', 'POST': 'table'},
        '/peticion_insert': {'POST': 'insert'},
        '/peticion_update': {'PUT': 'edit', 'POST': 'update'},
        '/peticion_delete': {'POST': 'delete'},
    }

    def get_extra_data(self):
        aux = super().get_extra_data()
        aux['persona'] = PersonaManager(self.db).get_all()
        return aux

    def index(self):
        self.set_session()
        self.verif_privileges()
        result = self.manager(self.db).list_all()
        result['privileges'] = UsuarioManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
        result.update(self.get_extra_data())
        self.render(self.html_index, **result)
        self.db.close()

    def insert(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        diccionary['fkestudiante'] = self.get_user_id()
        fecha = fecha_zona
        diccionary['fecha'] = fecha
        objeto = self.manager(self.db).entity(**diccionary)
        PeticionManager(self.db).insert(objeto)
        self.respond(success=True, message='Insertado correctamente.')

    def update(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        objeto = self.manager(self.db).entity(**diccionary)
        PeticionManager(self.db).update(objeto)
        self.respond(success=True, message='Modificado correctamente.')
