﻿# -*- coding: utf-8 -*-
##############################################################################
#
#    Perpul
#    Copyright (C) 2014-2016 CodUP (<http://codup.com>).
#
##############################################################################

from flectra.service.server import ThreadedServer
from flectra import api, fields, models


class cron_start_cron(models.TransientModel):
    _name = 'cron.start.cron'
    _description = 'Start cron'

    def start_cron(self):
        ThreadedServer(None).cron_spawn()
        return {'type': 'ir.actions.act_window_close',}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:        