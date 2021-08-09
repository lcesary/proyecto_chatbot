from server.database.connection import transaction
from server.persona.models import *
from server.persona.managers import *
from server.usuarios.models import *

import schedule


def insertions():

    with transaction() as session:

        ###Modulo de ubicacion

        pago_m = session.query(Modulo).filter(Modulo.name == 'Pagos').first()
        if pago_m is None:
            pago_m = Modulo(title='Modulo Pagos', name='Pagos', icon='book')


        m_pago = session.query(Modulo).filter(Modulo.name == 'pago').first()
        if m_pago is None:
            m_pago = Modulo(title='Administrar Pagos', route='/pago', name='pago',
                                    icon='portrait')

        pago_m.children.append(m_pago)

        query_pago = session.query(Modulo).filter(Modulo.name == 'pago_query').first()
        if query_pago is None:
            query_pago = Modulo(title='Consultar', route='',
                                    name='pago_query',
                                    menu=False)

        insert_pago = session.query(Modulo).filter(Modulo.name == 'pago_insert').first()
        if insert_pago is None:
            insert_pago = Modulo(title='Adicionar', route='/pago_insert',
                                     name='pago_insert',
                                     menu=False)

        update_pago = session.query(Modulo).filter(Modulo.name == 'pago_update').first()
        if update_pago is None:
            update_pago = Modulo(title='Actualizar', route='/pago_update',
                                     name='pago_update',
                                     menu=False)

        delete_pago= session.query(Modulo).filter(Modulo.name == 'pago_delete').first()
        if delete_pago is None:
            delete_pago = Modulo(title='Dar de Baja', route='/pago_delete',
                                     name='pago_delete',
                                     menu=False)

            m_pago.children.append(query_pago)
            m_pago.children.append(insert_pago)
            m_pago.children.append(update_pago)
            m_pago.children.append(delete_pago)

        admin_role = session.query(Rol).filter(Rol.nombre == 'ADMINISTRADOR').first()

        ###Modulos de Operaciones

        admin_role.modulos.append(pago_m)

        admin_role.modulos.append(m_pago)

        admin_role.modulos.append(query_pago)
        admin_role.modulos.append(insert_pago)
        admin_role.modulos.append(update_pago)
        admin_role.modulos.append(delete_pago)
        session.commit()



