from server.database.connection import transaction
from server.persona.models import *
from server.persona.managers import *
from server.usuarios.models import *

import schedule


def insertions():

    with transaction() as session:

        ###Modulo de Operaciones

        persona_m = session.query(Modulo).filter(Modulo.name == 'persona').first()
        if persona_m is None:
            persona_m = Modulo(title='Modulo Persona', name='persona', icon='book')


        solicitud_m = session.query(Modulo).filter(Modulo.name == 'solicitud').first()
        if solicitud_m is None:
            solicitud_m = Modulo(title='Modulo SOS', name='solicitud', icon='book')


        m_persona = session.query(Modulo).filter(Modulo.name == 'personal').first()
        if m_persona is None:
            m_persona = Modulo(title='Datos Persona', route='/personal', name='personal',
                                    icon='portrait')

        persona_m.children.append(m_persona)

        m_peticion = session.query(Modulo).filter(Modulo.name == 'peticion').first()
        if m_peticion is None:
            m_peticion = Modulo(title='SOS', route='/peticion', name='peticion',
                               icon='portrait')
        m_ubicacioin = session.query(Modulo).filter(Modulo.name == 'ubicacion').first()
        if m_ubicacioin is None:
            m_ubicacioin = Modulo(title='Ubicacion', route='/ubicacion', name='ubicacicn',
                                icon='portrait')

        solicitud_m.children.append(m_peticion)
        solicitud_m.children.append(m_ubicacioin)


        query_persona = session.query(Modulo).filter(Modulo.name == 'personal_query').first()
        if query_persona is None:
            query_persona = Modulo(title='Consultar', route='',
                                    name='personal_query',
                                    menu=False)

        insert_persona = session.query(Modulo).filter(Modulo.name == 'personal_insert').first()
        if insert_persona is None:
            insert_persona = Modulo(title='Adicionar', route='/personal_insert',
                                     name='personal_insert',
                                     menu=False)

        update_persona = session.query(Modulo).filter(Modulo.name == 'personal_update').first()
        if update_persona is None:
            update_persona = Modulo(title='Actualizar', route='/personal_update',
                                     name='personal_update',
                                     menu=False)

        delete_persona = session.query(Modulo).filter(Modulo.name == 'personal_delete').first()
        if delete_persona is None:
            delete_persona = Modulo(title='Dar de Baja', route='/personal_delete',
                                     name='personal_delete',
                                     menu=False)

        imprimir_persona = session.query(Modulo).filter(Modulo.name == 'personal_imprimir').first()
        if imprimir_persona is None:
            imprimir_persona = Modulo(title='Imprimir', route='/personal_imprimir',
                                       name='personal_imprimir',
                                       menu=False)

            m_persona.children.append(query_persona)
            m_persona.children.append(insert_persona)
            m_persona.children.append(update_persona)
            m_persona.children.append(delete_persona)
            m_persona.children.append(imprimir_persona)


        query_peticion = session.query(Modulo).filter(Modulo.name == 'peticion_query').first()
        if query_peticion is None:
            query_peticion = Modulo(title='Consultar', route='',
                                   name='peticion_query',
                                   menu=False)

        insert_peticion = session.query(Modulo).filter(Modulo.name == 'peticion_insert').first()
        if insert_peticion is None:
            insert_peticion = Modulo(title='Adicionar', route='/peticion_insert',
                                    name='peticion_insert',
                                    menu=False)

        update_peticion = session.query(Modulo).filter(Modulo.name == 'peticion_update').first()
        if update_peticion is None:
            update_peticion = Modulo(title='Actualizar', route='/peticion_update',
                                    name='peticion_update',
                                    menu=False)

        delete_peticion = session.query(Modulo).filter(Modulo.name == 'peticion_delete').first()
        if delete_peticion is None:
            delete_peticion = Modulo(title='Dar de Baja', route='/peticion_delete',
                                    name='peticion_delete',
                                    menu=False)

        imprimir_peticion = session.query(Modulo).filter(Modulo.name == 'peticion_imprimir').first()
        if imprimir_peticion is None:
            imprimir_peticion = Modulo(title='Imprimir', route='/peticion_imprimir',
                                      name='peticion_imprimir',
                                      menu=False)

            m_peticion.children.append(query_peticion)
            m_peticion.children.append(insert_peticion)
            m_peticion.children.append(update_peticion)
            m_peticion.children.append(delete_peticion)
            m_peticion.children.append(imprimir_peticion)



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

        delete_ubicacion  = session.query(Modulo).filter(Modulo.name == 'ubicacion_delete').first()
        if delete_ubicacion is None:
            delete_ubicacion = Modulo(title='Dar de Baja', route='/ubicacion_delete',
                                     name='ubicacion_delete',
                                     menu=False)

        imprimir_ubicacion = session.query(Modulo).filter(Modulo.name == 'ubicacion_imprimir').first()
        if imprimir_ubicacion is None:
            imprimir_ubicacion = Modulo(title='Imprimir', route='/ubicacion_imprimir',
                                       name='ubicacion_imprimir',
                                       menu=False)

            m_peticion.children.append(query_ubicacion)
            m_peticion.children.append(insert_ubicacion)
            m_peticion.children.append(update_ubicacion)
            m_peticion.children.append(delete_ubicacion)
            m_peticion.children.append(imprimir_ubicacion)

        admin_role = session.query(Rol).filter(Rol.nombre == 'ADMINISTRADOR').first()

        ###Modulos de Operaciones

        admin_role.modulos.append(persona_m)
        admin_role.modulos.append(solicitud_m)

        admin_role.modulos.append(m_persona)
        admin_role.modulos.append(m_peticion)
        admin_role.modulos.append(m_ubicacioin)

        admin_role.modulos.append(query_persona)
        admin_role.modulos.append(insert_persona)
        admin_role.modulos.append(update_persona)
        admin_role.modulos.append(delete_persona)
        admin_role.modulos.append(imprimir_persona)


        admin_role.modulos.append(query_peticion)
        admin_role.modulos.append(insert_peticion)
        admin_role.modulos.append(update_peticion)
        admin_role.modulos.append(delete_peticion)
        admin_role.modulos.append(imprimir_peticion)

        admin_role.modulos.append(query_ubicacion)
        admin_role.modulos.append(insert_ubicacion)
        admin_role.modulos.append(update_ubicacion)
        admin_role.modulos.append(delete_ubicacion)
        admin_role.modulos.append(imprimir_ubicacion)
        session.commit()



