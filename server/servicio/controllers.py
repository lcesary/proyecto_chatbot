
from tornado.gen import coroutine

from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError
from ..common.controllers import CrudController, SuperController, ApiController
import os.path
from ..usuarios.controllers import *
from ..ubicacion.managers import *

class ApiUsuarioController(ApiController):

    manager = UsuarioManager
    ubicacion = UbicacionManager
    routes = {
        '/api/v1/listar_usuario': {'GET': 'listar_usuarios'},
        '/api/v1/editar_usuario': {'POST': 'update_usuarios'},
        '/api/v1/crear_usuario': {'POST': 'insert'},
        '/api/v1/delete_usuario': {'POST': 'delete_usuarios'},
        '/api/v1/crear_peticion': {'POST': 'crear_peticion'},
        '/api/v1/login_usuario_mobile': {'POST': 'login_usuario_mobile'},
        '/api/v1/guardar_ubicacion': {'POST': 'guardar_ubicacion'},
        '/api/v1/guardar_carrera': {'POST': 'guardar_carrera'},
        '/api/v1/guardar_usuario': {'POST': 'guardar_usuario'},
        '/api/v1/ubicacion_carrera': {'POST': 'ubicacion_carrera'},
        '/api/v1/ubicacion_carrera_detalle': {'POST': 'ubicacion_carrera_detalle'},
    }

    def ubicacion_carrera(self):
        self.set_session()
        try:
            response = []
            data = json.loads(self.request.body.decode('utf-8'))
            fecha = UbicacionManager(self.db).fecha_actual()
            respuesta = CarreraManager(self.db).list_todo()
            for r in respuesta:
                sessions=list()
                a =  dict(id = r.id,conductor=r.conductor,monto=r.monto,tipo=r.tipo,tracks= ["Food"],)
                sessions.append(a)
                r = r.get_dict()
                diccionary = dict(fecha= r['fecha'],sessions=sessions)
                response.append(diccionary)
            self.respond(response=response, success=True, message="Usuario recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(success=False, message="Ocurrio un error.")
        self.db.close()

    def ubicacion_carrera_detalle(self):
        self.set_session()
        try:
            response = []
            data = json.loads(self.request.body.decode('utf-8'))
            respuesta = Detalle_carreraManager(self.db).listar_id(data['id'])
            for r in respuesta:
                r = r.get_dict()
                response.append(r)
            self.respond(response=response, success=True, message="Usuario recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(success=False, message="Ocurrio un error.")
        self.db.close()

    def check_xsrf_cookie(self):
        return

    def guardar_carrera(self):
        self.set_session()
        try:
            response = []
            data = json.loads(self.request.body.decode('utf-8'))
            fecha = UbicacionManager(self.db).fecha_actual()
            respuesta = CarreraManager(self.db).insert(data,fecha)
            self.respond(response=data, success=True, message="Usuario recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(success=False, message="Ocurrio un error.")
        self.db.close()

    def guardar_ubicacion(self):
        self.set_session()
        try:
            response = []
            data = json.loads(self.request.body.decode('utf-8'))
            objetos = UbicacionManager(self.db).listar_id(data['usuario'])
            if objetos != None:
                objetos.latitud = data['latitud']
                objetos.longitud = data['longitud']
            else:
                objetos = UbicacionManager(self.db).entity(**data)
                objetos = Ubicacion(cliente=objetos.usuario, latitud=str(objetos.latitud), longitud=str(objetos.longitud))
            respuesta = UbicacionManager(self.db).insert(objetos)
            self.respond(response=data, success=True, message="Usuario recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(success=False, message="Ocurrio un error.")
        self.db.close()

    def login_usuario_mobile(self):
        self.set_session()
        try:
            response = []
            data = json.loads(self.request.body.decode('utf-8'))
            validar = UsuarioManager(self.db).validar_usuario(data['username'],data['password'])
            if validar == 1:
                r  = UsuarioManager(self.db).listar_usuario(data['username'])
                self.respond(response=r.get_dict(), success=True, message="Usuario recuperados correctamente.")
            else:
                r = None
                self.respond(response=validar, success=False, message="Datos del usuario son incorrecto.")
        except Exception as e:
            print(e)
            self.respond(success=False, message="Ocurrio un error.")
        self.db.close()

    def guardar_usuario(self):
        self.set_session()
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            result = self.manager(self.db).listar_usuario(data['username'])
            response = []
            if result == None:
                objeto = self.manager(self.db).entity(**data)
                UsuarioManager(self.db).insertar(objeto)
                self.respond(response=response, success=True, message="Usuario recuperados correctamente.")
            else:
                self.respond(response=response, success=False, message="Ocurrio un problema.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message="Not Found")
        self.db.close()

    def listar_usuarios(self):
        self.set_session()
        try:
            result = self.manager(self.db).listar()
            response = []
            for usuario in result:
                dic = dict(id=str(usuario.id), nombre=str(usuario.nombre),
                           correo=str(usuario.correo),
                           username=str(usuario.username), rol=str(usuario.fkrol),
                           persona =str(usuario.fkpersona), apellido=str(usuario.apellido),
                           enabled=str(usuario.enabled), password=str(usuario.password))
                response.append(dic)
            self.db.close()
            self.respond(response=response, success=True, message="Usuario recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message="Not Found")
        self.db.close()


    def update_usuarios(self):
        data = json.loads(self.request.body.decode('utf-8'))
        self.set_session()
        response = []
        diccionary = dict(id=int(data['id']), nombre=data['nombre'],
                          username=data['username'], fkrol=int(data['rol']),
                          persona=data['persona'], enabled=data['enabled'],
                          correo=data['correo'], ip="123.123.123.123",
                          password=data['contraseña'])
        response.append(diccionary)
        objeto = self.manager(self.db).entity(**diccionary)
        self.manager(self.db).update(objeto)
        self.respond(response=response,success=True, message='Usuario Modificada correctamente.')
        self.db.close()

    def delete_usuarios(self):
        data = json.loads(self.request.body.decode('utf-8'))
        self.set_session()
        response = []
        diccionary = dict(id=int(data['id']), nombre=data['nombre'],
                          username=data['username'], fkrol=int(data['rol']),
                          persona=data['persona'], enabled=data['enabled'],
                          correo=data['correo'], ip="123.123.123.123")
        response.append(diccionary)
        objeto = self.manager(self.db).entity(**diccionary)
        self.manager(self.db).update(objeto)
        self.respond(response=response,success=True, message='Usuario Modificada correctamente.')
        self.db.close()

    def insert(self):
        data = json.loads(self.request.body.decode('utf-8'))
        try:
            response = []
            self.set_session()
            diccionary = dict(nombre=data['nombre'],
                              username=data['username'], fkrol=int(data['rol']),
                              apellido=data['apellido'],
                              persona=data['persona'], correo=data['correo'],
                              ip=data['ip'],password=data['password'],user_id=int(data['id']),)
            response.append(diccionary)
            objeto = self.manager(self.db).entity(**diccionary)
            self.manager(self.db).insert(objeto)
            self.respond(response=response, success=True, message='Insertado correctamente.')
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message="Not Found")
        self.db.close()

