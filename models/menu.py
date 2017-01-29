#import inspect
#all_functions = inspect.getmembers(sustancias, inspect.isfunction)

app = request.application
response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Home'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Modules'),False,None,[
        (T('SMyDP'),URL('front_page','index'),URL('front_page','index')),
        ]),
(T('Editar'), False, URL('admin', 'default', 'design/%s' % app)),
#(T('Personal'),URL('default','personal_manage')==URL(),URL('default','personal_manage'),[]),
#(T('Rol'),URL('default','rol_manage')==URL(),URL('default','rol_manage'),[]),
#(T('Sustancia'),URL('default','sustancia_manage')==URL(),URL('default','sustancia_manage'),[]),
#(T('Secciones'),URL('default','secciones_manage')==URL(),URL('default','secciones_manage'),[]),
#(T('Laboratorio'),URL('default','laboratorio_manage')==URL(),URL('default','laboratorio_manage'),[]),
#(T('Bitacora'),URL('default','bitacora_manage')==URL(),URL('default','bitacora_manage'),[]),
#(T('Solicitudes'),URL('default','solicitudes_manage')==URL(),URL('default','solicitudes_manage'),[]),
#(T('Sustanciapeligrosa'),URL('default','sustanciapeligrosa_manage')==URL(),URL('default','sustanciapeligrosa_manage'),[]),
#(T('Cargo'),URL('default','cargo_manage')==URL(),URL('default','cargo_manage'),[]),
#(T('Inventario'),URL('default','inventario_manage')==URL(),URL('default','inventario_manage'),[]),
#(T('Solicitud'),URL('default','solicitud_manage')==URL(),URL('default','solicitud_manage'),[]),
]