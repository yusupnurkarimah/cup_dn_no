# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    no_dn_inv = fields.Char(string='No DN', readonly=True)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    no_dn_so = fields.Char(string='No DN', readonly=True, states={"draft" : [("readonly",False)]})

    def _create_invoices(self , grouped=False, final=False):
        res = super(SaleOrder, self)._create_invoices(grouped=grouped, final=final)
        for rec in self:
            obj = self.env['account.move'].search([('invoice_origin','=',rec.name)])
            for record in obj:
                record.no_dn_inv = rec.no_dn_so

        return res