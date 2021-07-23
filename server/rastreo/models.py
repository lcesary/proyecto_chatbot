from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, BigInteger, Text
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime

from ..database.models import Base
from ..database.serializable import Serializable
import pytz
from ..persona.models import *

global fecha_zona
fecha_zona = datetime.now(pytz.timezone('America/La_Paz'))


class Ubicacion(Serializable, Base):
    way = {}

    __tablename__ = 'cb_rastreo'

    id = Column(Integer, primary_key=True)
    fkpersona = Column(Integer, ForeignKey('cb_persona.id'))
    latitud = Column(Float, nullable=False)
    longitud = Column(Float, nullable=False)

    persona = relationship('Persona')




