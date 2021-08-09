import sqlite3
import sys
from configparser import ConfigParser

from sqlalchemy.engine import create_engine

from server.database import connection
from server.persona.scripts import insertions as mpersonal_insertions
from .models import Base
from ..usuarios.scripts import insertions as user_insertions
from ..chat.scripts import insertions as chat_insertions
from ..ubicacion.scripts import insertions as ubicacion_insertions
from ..pago.scripts import insertions as pago_insertions

def main():
    reload_db()
    user_insertions()
    # mpersonal_insertions()
    chat_insertions()
    ubicacion_insertions()
    pago_insertions()
    print('Database created/updated correctly!')


def reload_db():
    config = ConfigParser()
    config.read('settings.ini')
    db_url = config['Database']['url']
    connection.db_url = config['Database']['url']
    if 'sqlite' in db_url:
        dbname = db_url.split('///')[1]
        sqlite3.connect(dbname)
    engine = create_engine(config['Database']['url'])
    Base.metadata.drop_all(engine, checkfirst=True)
    Base.metadata.create_all(engine, checkfirst=True)


if __name__ == '__main__':
    sys.exit(int(main() or 0))
