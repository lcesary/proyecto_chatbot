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



class Chat(Serializable,Base):
    way = {'Usuario': {}}

    __tablename__ = 'cb_chat'
    id = Column(Integer, primary_key=True)
    fecha = Column('fecha', DateTime, nullable=True)
    texto = Column('texto', String(500), nullable=False)
    emisorc = Column('emisorc', Integer)
    emisoru = Column('emisoru', Integer, ForeignKey('cb_usuarios_usuario.cb_usuario_id'), nullable=True)

    usuario = relationship('Usuario')


