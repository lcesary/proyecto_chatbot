import os
from .usuarios.controllers import *
from .persona.controllers import *
from .operaciones.controllers import *
from .main.controllers import Index
from tornado.web import StaticFileHandler
from .operaciones.controllers import *
from .rastreo.controllers import *
from .servicio.controllers import *

def get_handlers():
    """Retorna una lista con las rutas, sus manejadores y datos extras."""
    handlers = list()
    # Login
    handlers.append((r'/login', LoginController))
    handlers.append((r'/logout', LogoutController))
    handlers.append((r'/manual', ManualController))

    # Principal
    handlers.append((r'/', Index))

    # Usuario
    handlers.extend(get_routes(UsuarioController))
    handlers.extend(get_routes(RolController))

    # MCatalogo
    handlers.extend(get_routes(PersonaController))
    handlers.extend(get_routes(PeticionController))
    handlers.extend(get_routes(UbicacionController))

    handlers.extend(get_routes(BitacoraController))


    #servicio Movil
    handlers.extend(get_routes(ApiUsuarioController))

    handlers.append((r'/resources/(.*)', StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'common', 'resources')}))
    return handlers


def get_routes(handler):
    routes = list()
    for route in handler.routes:
        routes.append((route, handler))
    return routes
