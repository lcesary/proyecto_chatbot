from sqlalchemy import Column, Integer, String, Boolean,Float
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.orm import relationship

from ..database.models import Base
from ..database.serializable import Serializable


class Usuario(Serializable, Base):
    way = {'rol': {'modulos': {}}}

    __tablename__ = 'cb_usuarios_usuario'

    id = Column('cb_usuario_id', Integer, primary_key=True)
    nombre = Column('cb_usuario_nombre', String(50), nullable=False)
    apellido = Column('cb_usuario_apellido', String(50), nullable=False)
    correo = Column('cb_usuario_correo', String(100), nullable=False)
    username = Column('cb_usuario_username', String(50), nullable=False, unique=True)
    password = Column('cb_usuario_password', String(150), nullable=False)
    fkrol = Column('cb_usuario_fkrol', Integer, ForeignKey('cb_usuarios_rol.cb_rol_id'), nullable=False)
    activo = Column('cb_usuario_activo', Integer, default=0)
    token2 = Column('cb_usuario_token2', String(2000), nullable=True, default='Sin Token2')
    token = Column('cb_usuario_token', String(2000), nullable=True, default='Sin Token')
    foto = Column('foto',String(2000),nullable=False,default='resources/images/sinImagen.jpg')
    enabled = Column('cb_usuario_enabled', Boolean, default=True)
    monto = Column('monto', Float, default=0)


    rol = relationship('Rol')


    def get_dict(self, way=None):
        dictionary = super().get_dict(way)
        del(dictionary['password'])
        return dictionary


Acceso = Table('cb_usuarios_acceso', Base.metadata,
               Column('cb_acceso_id', Integer, primary_key=True),
               Column('cb_acceso_fkrol', Integer, ForeignKey('cb_usuarios_rol.cb_rol_id')),
               Column('cb_acceso_fkmodulo', Integer, ForeignKey('cb_usuarios_modulo.cb_modulo_id')))


class Rol(Serializable, Base):
    way = {'usuario': {}, 'modulos': {}}

    __tablename__ = 'cb_usuarios_rol'

    id = Column('cb_rol_id', Integer, primary_key=True)
    nombre = Column('cb_rol_nombre', String(50), nullable=False)
    descripcion = Column('cb_rol_descripcion', String(200), nullable=False)
    enabled = Column('cb_rol_enabled', Boolean, default=True)

    usuario = relationship('Usuario')
    modulos = relationship('Modulo', secondary=Acceso)


class Modulo(Serializable, Base):
    way = {'roles': {}}

    __tablename__ = 'cb_usuarios_modulo'

    id = Column('cb_modulo_id', Integer, primary_key=True)
    route = Column('cb_modulo_route', String(100))
    title = Column('cb_modulo_title', String(100), nullable=False)
    name = Column('cb_modulo_name', String(100), nullable=False, unique=True)
    icon = Column('cb_modulo_icon', String(50), nullable=False, default='home')
    menu = Column('cb_modulo_menu', Boolean, nullable=False, default=True)
    fkmodulo = Column('cb_modulo_fkmodulo', Integer, ForeignKey('cb_usuarios_modulo.cb_modulo_id'))

    roles = relationship('Rol', secondary=Acceso)
    children = relationship('Modulo')
