import hashlib
import string
from random import *
import json
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import make_transient
import random
from ..database.connection import transaction
from ..usuarios.models import *
from server.common.managers import SuperManager
from .models import *
from sqlalchemy.sql import func, extract, cast, text
from sqlalchemy import Date
from datetime import datetime, date, time, timedelta
from pyfcm import FCMNotification
import pytz

import uuid
from server.common.managers import Error
from server.database.connection import transaction
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

global fecha_zona
#fecha_zona = datetime.now(pytz.timezone('America/La_Paz'))
fecha_zona = datetime.now()


class UbicacionManager(SuperManager):
    def __init__(self, db):
        super().__init__(Ubicacion, db)

    def listar_id(self,id):
        a = self.db.query(Ubicacion).filter(Ubicacion.cliente == id).first()
        return a

    def list_all(self):
        return dict(objects=self.db.query(Ubicacion).order_by(Ubicacion.id.asc()))

    def fecha_actual(self):
        return datetime.now(pytz.timezone('America/La_Paz'))

    def fecha(self):
        return fecha_zona.strftime('%Y/%d/%m')

    def insert(self, object):
        return super().insert(object)

class Detalle_carreraManager(SuperManager):
    def __init__(self, db):
        super().__init__(Detalle_carrera, db)

    def insert(self, objeto,carrera):
        detalle_carrera = Detalle_carrera(fecha=carrera.fecha, monto=carrera.monto,origlat=objeto['origen']['lat'],origlon=objeto['origen']['lng'],deslat=objeto['destino']['lat'],deslon=objeto['destino']['lng'],fk_usuario=objeto['usuario'],fk_carrera=carrera.id)
        detalle_carrera = super().insert(detalle_carrera)
        return detalle_carrera.get_dict()

    def listar_id(self,id):
        a = self.db.query(Detalle_carrera).filter(Detalle_carrera.fk_carrera == id).all()
        return a

class CarreraManager(SuperManager):
    def __init__(self, db):
        super().__init__(Carrera, db)

    def insert(self, objeto, fecha):
        carrera = Carrera(fecha=fecha, monto=objeto['costo'], tipo=objeto['tipo'], enabled=0)
        carrera = super().insert(carrera)
        detalle =Detalle_carreraManager(self.db).insert(objeto,carrera)
        carrera = carrera.get_dict()
        carrera['detalle']=detalle
        return carrera

    def list_all(self):
        return dict(objects=self.db.query(Carrera).order_by(Carrera.id.asc()).all())

    def list_todo(self):
        return self.db.query(Carrera).filter(Carrera.enabled == 0).all()

    def fecha_actual(self):
        return datetime.now(pytz.timezone('America/La_Paz'))

    def fecha(self):
        return fecha_zona.strftime('%Y/%d/%m')

