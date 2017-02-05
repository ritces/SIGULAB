# -*- coding: utf-8 -*-
from gluon.tools import Crud

@auth.requires_login()
def sustanciapeligrosa_manage():
    if(auth.has_permission('gestor','t_sustancias') or \
    auth.has_permission('director','t_sustancias')):
        table = SQLFORM.smartgrid(db.t_sustancias,onupdate=auth.archive,details=False,links_in_grid=False,csv=False,user_signature=True)
    else:
        table = SQLFORM.smartgrid(db.t_sustancias,editable=False,deletable=False,csv=False,links_in_grid=False,create=False)
    return locals()

@auth.requires_login()
def select_inventario():
    #if (auth.has_membership('tecnico')):
    espacios = db(db.t_espaciofisico.f_tecnico == auth.user.id).select(db.t_espaciofisico.f_espacio, db.t_espaciofisico.id)
    return locals()



@auth.requires_login()
def inventario_manage():
    espF = request.vars['esp']
    query = db.t_inventario.f_espaciofisico == espF
    if(auth.has_permission('tecnico','t_inventario')):

        table = SQLFORM.smartgrid(db.t_inventario,create=False,links_in_grid=False,csv=False,editable=False,deletable=False,details=False)
    else:
        table = SQLFORM.smartgrid(db.t_inventario,constraints=dict(t_inventario=query),onupdate=auth.archive)
    return locals()

@auth.requires_login()
def view_bitacora():
    sust = request.vars['sust']

    name = str(db(db.t_sustancias.id == sust).select(db.t_sustancias.f_nombre))[22:]
    #espF = str(db(db.t_espaciofisico.f_tecnico == 3).select(db.t_espaciofisico.id))[20:]
    total = str((db((db.t_inventario.f_sustancia == sust)&(db.t_inventario.f_espaciofisico == espF)).select(db.t_inventario.f_cantidadusointerno)))[34:]
    #total = str(total)[34:]
    #for row in db((db.t_bitacora.f_sustancia == name)&
    #            (db.t_bitacora.espaciofisico == db.t_inventario.espaciofisico)).select(db.t_inventario.ALL,db.t_bitacora.cantidad):

    #rows = db((db.t_bitacora.f_sustancia == sust)&(db.t_bitacora.f_espaciofisico == espF)).select(db.t_bitacora.f_fecha,
    #db.t_bitacora.f_proceso,db.t_bitacora.f_ingreso,db.t_bitacora.f_consumo,db.t_bitacora.f_cantidad)
    db.t_bitacora.f_espaciofisico.readable
    db.t_bitacora.f_sustancia.default = sust
    db.t_bitacora.f_espaciofisico.default = espF
    db.t_bitacora.f_espaciofisico.readable = False
    query = (db.t_bitacora.f_sustancia == sust)
    #table.vars.f_sustancia.default = sust
    #table.vars.f_espaciofisico.default = espF
    table = SQLFORM.smartgrid(db.t_bitacora,constraints=dict(t_bitacora=query),
    orderby=~db.t_bitacora.f_fecha,details=False,csv=False,links_in_grid=False,deletable=False,
    user_signature=True)
    #table.vars.f_espaciofisico.default = espF
    #table.vars.f_sustancia.default = sust
    #table = SQLFORM.grid(query)
    #table = SQLTABLE(rows, headers='fieldname:capitalize', _width="100%")
    return locals()
