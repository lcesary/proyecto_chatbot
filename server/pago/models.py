from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, BigInteger, Text
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime

from ..database.models import Base
from ..database.serializable import Serializable
import pytz

global fecha_zona
fecha_zona = datetime.now(pytz.timezone('America/La_Paz'))


class Pago(Serializable, Base):
    way = {'usuario': {}}

    __tablename__ = 'pago'

    id = Column('id', Integer, primary_key=True)
    cliente = Column('cliente', Integer, ForeignKey('cb_usuarios_usuario.cb_usuario_id'), nullable=False)
    conductor = Column('conductor', Integer, nullable=False)
    fecha = Column('fecha', DateTime, nullable=False, default=fecha_zona)
    monto = Column('monto', Integer, nullable=True)

    usuario = relationship('Usuario')