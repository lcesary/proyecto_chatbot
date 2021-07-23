import hashlib
import string
from _ast import In, GeneratorExp
from random import *
from ..operaciones.models import *
from datetime import datetime, timedelta, time, date
from ..operaciones.managers import *
from .models import *
import json
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import make_transient, sessionmaker
import random
from ..database.connection import transaction
from ..usuarios.models import *
from server.common.managers import SuperManager
from .models import *

from ..usuarios.managers import *

global image_report
image_report = 'server/common/resources/images/sabsa-xls.png'


class PersonaManager(SuperManager):
    def __init__(self, db):
        super().__init__(Persona, db)

    def obtener_x_codigo(self, codigo):
        return self.db.query(self.entity).filter(self.entity.codigo == codigo).first()

    def get_all(self):
        return self.db.query(self.entity).filter(self.entity.enabled == True).all()

    def list_all(self):
        return dict(objects=self.db.query(self.entity).filter(self.entity.enabled == True))

    def listar_todo(self):
        return self.db.query(self.entity).filter(self.entity.enabled == True)

    def insert(self, objeto):
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().insert(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Registro una Persona.", fecha=fecha,tabla="cb_persona", identificador=a.id)
        super().insert(b)
        return a

    def update(self, objeto):
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Modifico una Persona.", fecha=fecha,tabla="cb_persona", identificador=a.id)
        super().insert(b)
        return a

    def delete(self, id, user, ip):
        x = self.db.query(self.entity).filter(self.entity.id == id).one()
        x.enabled = False
        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion="Eliminó una persona.", fecha=fecha,tabla="cb_persona", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()

    def obtener_x_tipo(self, nombre):
        a = dict(etudiante=self.db.query(self.entity).filter(self.entity.tipo == nombre).filter(self.entity.enabled == True))
        return a
    def insertarpersona(self,objecto,fkpersona):
        b = Personal(especialidad=objecto.especialidad, cargo=objecto.cargo, transporte=objecto.transporte, fkpersona=fkpersona
                     ,user=objecto.user, ip=objecto.ip,)
        return b

class PersonalManager(SuperManager):
    def __init__(self, db):
        super().__init__(Personal, db)

    def get_all(self):
        return self.db.query(self.entity).filter(self.entity.enabled == True).all()

    def list_all(self):
        return dict(objects=self.db.query(self.entity).filter(self.entity.enabled == True))

    def listar_todo(self):
        return self.db.query(self.entity).filter(self.entity.enabled == True)

    def insert(self, objeto):
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().insert(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Registro un Personal.", fecha=fecha,
                     tabla="cb_personal", identificador=a.id)
        super().insert(b)
        return a

    def update(self, objeto):
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Modifico un Persona.", fecha=fecha,
                     tabla="cb_personal", identificador=a.id)
        super().insert(b)
        return a

    def delete(self, id, user, ip):
        x = self.db.query(self.entity).filter(self.entity.id == id).one()
        x.enabled = False
        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion="Eliminó un Persona.", fecha=fecha,
                     tabla="cb_persona", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()


class PeticionManager(SuperManager):
    def __init__(self, db):
        super().__init__(Peticion, db)

    def obtener_x_nombre(self, nombre):
        try:
            return self.db.query(self.entity).filter(self.entity.nombre == nombre).first()
        except Exception as ex:
            return "No hay"

    def get_all(self):
        return self.db.query(self.entity).filter(self.entity.enabled == True).all()

    def list_all(self):
        return dict(objects=self.db.query(self.entity).filter(self.entity.enabled == True))

    def listar_todo(self):
        return self.db.query(self.entity).filter(self.entity.enabled == True)

    def insert(self, objeto):
        fecha = BitacoraManager(self.db).fecha_actual()
        a = super().insert(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Registro una Peticion.", fecha=fecha,
                     tabla="cb_peticion", identificador=a.id)
        super().insert(b)
        return a

    def update(self, objeto):
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Modifico una Peticion.", fecha=fecha,
                     tabla="cb_peticion", identificador=a.id)
        super().insert(b)
        return a

    def delete(self, id, user, ip):
        x = self.db.query(self.entity).filter(self.entity.id == id).one()
        x.enabled = False
        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion="Eliminó una Peticion.", fecha=fecha, tabla="cb_peticion",
                     identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()

