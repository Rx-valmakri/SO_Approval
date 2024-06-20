# -*- coding: utf-8 -*-
from odoo import models, fields


class WarningMessage(models.TransientModel):
    _name = 'warning.message'

    message_text = fields.Text(string="GET APPROVAL FROM MANAGER", readonly=True)


