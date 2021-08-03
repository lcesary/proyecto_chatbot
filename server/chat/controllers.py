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



class ChatController(CrudController):

    manager = ChatManager
    html_index = "chat/views/index.html"
    html_table = "chat/views/table.html"
    routes = {
        '/chat': {'GET': 'index', 'POST': 'table'},
        '/chat_insert': {'POST': 'insert'},
        '/chat_update': {'PUT': 'edit', 'POST': 'update'},
        '/chat_delete': {'POST': 'delete'},
    }



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
        diccionary['ip'] = self.request.remote_ip
        diccionary['user'] = self.get_user_id()
        diccionary['emisorc'] = self.get_user_id()
        fecha = datetime.now()
        diccionary['fecha'] = fecha
        objeto = self.manager(self.db).entity(**diccionary)
        self.manager(self.db).insert(objeto)
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

