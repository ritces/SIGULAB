# -*- coding: utf-8 -*-
@auth.requires_login()
def sustanciapeligrosa_manage():
    if(auth.has_permission('gestor','t_sustanciapeligrosa')):
        table = SQLFORM.smartgrid(db.t_sustanciapeligrosa,onupdate=auth.archive)
    else:
        rows = db(db.t_sustanciapeligrosa).select(db.t_sustanciapeligrosa.f_nombre,
                                                  db.t_sustanciapeligrosa.f_cas,
                                                  db.t_sustanciapeligrosa.f_pureza,
                                                  db.t_sustanciapeligrosa.f_estado,
                                                  db.t_sustanciapeligrosa.f_control,
                                                  db.t_sustanciapeligrosa.f_peligrosidad)
        table = SQLTABLE(rows, headers='fieldname:capitalize',orderby=db.t_sustanciapeligrosa.f_pureza, _width="100%")
    return locals()
