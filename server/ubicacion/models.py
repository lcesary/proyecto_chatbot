from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, BigInteger, Text,DECIMAL
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime

from ..database.models import Base
from ..database.serializable import Serializable
import pytz

global fecha_zona
fecha_zona = datetime.now(pytz.timezone('America/La_Paz'))

class Ubicacion(Serializable, Base):
    way = {'usuario': {}}

    __tablename__ = 'ubicacion'
    id = Column(Integer, primary_key=True)
    cliente = Column(Integer, ForeignKey("cb_usuarios_usuario.cb_usuario_id"))
    latitud = Column(String(255), nullable=True)
    longitud = Column(String(255), nullable=True)
    estado = Column(String(255), nullable=False)
    tipo = Column(String(255), nullable=False)
    enabled = Column(Boolean, default=True)

    usuario = relationship('Usuario')


class Carrera(Serializable, Base):
    way = {'usuario': {}}

    __tablename__ = 'carrera'
    id = Column(Integer, primary_key=True)
    fecha = Column(DateTime, nullable=False)
    monto = Column(Float, nullable = False, default = 0)
    tipo = Column(String(255),nullable=False,default='Multiple')
    conductor = Column(Integer, ForeignKey("cb_usuarios_usuario.cb_usuario_id"))
    enabled = Column(Boolean, default=True)

    usuario = relationship('Usuario')

Acceso = Table('detalle_carrera', Base.metadata,
               Column('id', Integer, primary_key=True),
               Column('fk_usuario', Integer, ForeignKey('cb_usuarios_usuario.cb_usuario_id')),
               Column('fk_carrera', Integer, ForeignKey('carrera.id')),
               Column('monto', Float),
               Column('latitud',String(255), nullable=True),
               Column('longitud',String(255), nullable=True),
               Column('estado',Boolean,nullable=False,default=1))

