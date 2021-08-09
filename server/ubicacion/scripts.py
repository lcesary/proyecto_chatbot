from server.database.connection import transaction
from server.persona.models import *
from server.persona.managers import *
from server.usuarios.models import *

import schedule


def insertions():

    with transaction() as session:

        ###Modulo de ubicacion

        ubicacion_m = session.query(Modulo).filter(Modulo.name == 'ubicaciones').first()
        if ubicacion_m is None:
            ubicacion_m = Modulo(title='Modulo ubicaciones', name='ubicaciones', icon='book')


        m_ubicacion = session.query(Modulo).filter(Modulo.name == 'ubicacion').first()
        if m_ubicacion is None:
            m_ubicacion = Modulo(title='Administrar ubicaciones', route='/ubicacion', name='ubicacion',
                                    icon='portrait')

        m_carrera = session.query(Modulo).filter(Modulo.name == 'carrera').first()
        if m_carrera is None:
            m_carrera = Modulo(title='Administrar carreras', route='/carrera', name='carrera',
                                 icon='portrait')

        ubicacion_m.children.append(m_ubicacion)
        ubicacion_m.children.append(m_carrera)

        query_ubicacion = session.query(Modulo).filter(Modulo.name == 'ubicacion_query').first()
        if query_ubicacion is None:
            query_ubicacion = Modulo(title='Consultar', route='',
                                    name='ubicacion_query',
                                    menu=False)

        insert_ubicacion = session.query(Modulo).filter(Modulo.name == 'ubicacion_insert').first()
        if insert_ubicacion is None:
            insert_ubicacion = Modulo(title='Adicionar', route='/ubicacion_insert',
                                     name='ubicacion_insert',
                                     menu=False)

        update_ubicacion = session.query(Modulo).filter(Modulo.name == 'ubicacion_update').first()
        if update_ubicacion is None:
            update_ubicacion = Modulo(title='Actualizar', route='/ubicacion_update',
                                     name='ubicacion_update',
                                     menu=False)

        delete_ubicacion= session.query(Modulo).filter(Modulo.name == 'ubicacion_delete').first()
        if delete_ubicacion is None:
            delete_ubicacion = Modulo(title='Dar de Baja', route='/ubicacion_delete',
                                     name='ubicacion_delete',
                                     menu=False)

            m_ubicacion.children.append(query_ubicacion)
            m_ubicacion.children.append(insert_ubicacion)
            m_ubicacion.children.append(update_ubicacion)
            m_ubicacion.children.append(delete_ubicacion)

        query_carrera = session.query(Modulo).filter(Modulo.name == 'carrera_query').first()
        if query_carrera is None:
            query_carrera = Modulo(title='Consultar', route='',
                                     name='carrera_query',
                                     menu=False)

        insert_carrera = session.query(Modulo).filter(Modulo.name == 'carrera_insert').first()
        if insert_carrera is None:
            insert_carrera = Modulo(title='Adicionar', route='/carrera_insert',
                                      name='carrera_insert',
                                      menu=False)

        update_carrera = session.query(Modulo).filter(Modulo.name == 'carrera_update').first()
        if update_carrera is None:
            update_carrera = Modulo(title='Actualizar', route='/carrera_update',
                                      name='carrera_update',
                                      menu=False)

        delete_carrera = session.query(Modulo).filter(Modulo.name == 'carrera_delete').first()
        if delete_carrera is None:
            delete_carrera = Modulo(title='Dar de Baja', route='/carrera_delete',
                                      name='carrera_delete',
                                      menu=False)

            m_carrera.children.append(query_carrera)
            m_carrera.children.append(insert_carrera)
            m_carrera.children.append(update_carrera)
            m_carrera.children.append(delete_carrera)

        admin_role = session.query(Rol).filter(Rol.nombre == 'ADMINISTRADOR').first()

        ###Modulos de Operaciones

        admin_role.modulos.append(ubicacion_m)

        admin_role.modulos.append(m_ubicacion)
        admin_role.modulos.append(m_carrera)

        admin_role.modulos.append(query_ubicacion)
        admin_role.modulos.append(insert_ubicacion)
        admin_role.modulos.append(update_ubicacion)
        admin_role.modulos.append(delete_ubicacion)

        admin_role.modulos.append(query_carrera)
        admin_role.modulos.append(insert_carrera)
        admin_role.modulos.append(update_carrera)
        admin_role.modulos.append(delete_carrera)
        session.commit()



