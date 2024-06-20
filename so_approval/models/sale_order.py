# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[('waiting_for_approval', "Waiting For Approval"), ('sent',)])
    approve_check = fields.Boolean()

    # @api.onchange('order_line')
    # def onchange_order_line(self):
    #     for rec in self:
    #         for record in rec.order_line:
    #             if record.price_unit != record.product_id.lst_price:
    #                 rec.approve_check = True
    #             else:
    #                 rec.approve_check = False

    def action_confirm(self):
        for rec in self:
            for record in rec.order_line:
                if record.price_unit != record.product_id.lst_price and not rec.approve_check:
                    rec.write({'state': 'waiting_for_approval'})
                    return {
                        'name': 'warning.message.form.view',
                        'type': 'ir.actions.act_window',
                        'res_model': 'warning.message',
                        'view_mode': 'form',
                        'view_type': 'form',
                        'target': 'new'
                    }
                else:
                    return super().action_confirm()

    def action_disapprove(self):
        self.write({'state': 'draft'})
        self.approve_check = False

    def action_approve(self):
        self.approve_check = True
        self.write({'state': 'draft'})
        res = super().action_confirm()
        self.write({'state': 'sale'})
        return res


