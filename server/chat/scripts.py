from server.database.connection import transaction
from server.persona.models import *
from server.persona.managers import *
from server.usuarios.models import *

import schedule


def insertions():

    with transaction() as session:

        ###Modulo de Operaciones

        chat_m = session.query(Modulo).filter(Modulo.name == 'chat').first()
        if chat_m is None:
            chat_m = Modulo(title='Modulo Chat',route = '/chat', name='chat', icon='book')


        query_chat = session.query(Modulo).filter(Modulo.name == 'chat_query').first()
        if query_chat is None:
            query_chat = Modulo(title='Consultar', route='', name='chat_query', menu=False)

        insert_chat = session.query(Modulo).filter(Modulo.name == 'chat_insert').first()
        if insert_chat is None:
            insert_chat = Modulo(title='Adicionar', route='/chat_insert',name='chat_insert',menu=False)

        update_chat = session.query(Modulo).filter(Modulo.name == 'chat_update').first()
        if update_chat is None:
            update_chat = Modulo(title='Actualizar', route='/chat_update',
                                     name='chat_update',
                                     menu=False)

        delete_chat = session.query(Modulo).filter(Modulo.name == 'chat_delete').first()
        if delete_chat is None:
            delete_chat = Modulo(title='Dar de Baja', route='/chat_delete',
                                     name='chat_delete',
                                     menu=False)

            chat_m.children.append(query_chat)
            chat_m.children.append(insert_chat)
            chat_m.children.append(update_chat)
            chat_m.children.append(delete_chat)

        admin_role = session.query(Rol).filter(Rol.nombre == 'ADMINISTRADOR').first()

        ###Modulos de Operaciones

        admin_role.modulos.append(chat_m)

        admin_role.modulos.append(query_chat)
        admin_role.modulos.append(insert_chat)
        admin_role.modulos.append(update_chat)
        admin_role.modulos.append(delete_chat)

        session.commit()



