from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float, BigInteger, Text, Time
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime


from ..database.models import Base
from ..database.serializable import Serializable
from sqlalchemy.ext.hybrid import hybrid_property

import pytz

global fecha_zona
fecha_zona = datetime.now(pytz.timezone('America/La_Paz'))



class Persona(Serializable,Base):
    way = {}

    __tablename__ = 'cb_persona'
    id = Column(Integer, primary_key=True)
    codigo = Column(Integer, nullable=False)
    nombre = Column(String(50), nullable=True)
    apellido = Column(String(50), nullable=True)
    telefono = Column(Integer, nullable=True)
    sexo = Column(String(10), nullable=False)
    foto = Column(Text, nullable=True, default="Sin Foto")
    direccion = Column(String(50), nullable=False)
    tipo = Column(String(20), nullable=False)
    enabled = Column(Boolean, default=True)




class Personal(Serializable, Base):
    way = {'persona': {}}

    __tablename__ = 'cb_personal'
    id = Column(Integer, primary_key=True)
    especialidad = Column(String(50), nullable=False)
    cargo = Column(String(50), nullable=False)
    transporte = Column(String(50), nullable=False)
    enabled = Column(Boolean, default=True)


    fkpersona = Column(Integer, ForeignKey("cb_persona.id"))


class Peticion(Serializable, Base):
    way = {'personal': {}}

    __tablename__ = 'cb_peticion'
    id = Column(Integer, primary_key=True)
    fecha = Column(DateTime, nullable=False)
    peticion = Column(Text, nullable=False)
    fkestudiante = Column(Integer, ForeignKey("cb_persona.id"))
    fkpersonal = Column(Integer, ForeignKey("cb_personal.id"), default=None)
    estado = Column(Text, nullable=False)
    latitud = Column(Float, nullable=True)
    longitud = Column(Float, nullable=True)
    enabled = Column(Boolean, default=True)

    personal = relationship('Persona')
    persona = relationship('Personal')
