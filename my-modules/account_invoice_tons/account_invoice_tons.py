# -*- coding: utf-8 -*-

from openerp import models, fields, api

 class account_invoice_tons(models.Model):
     _inherit = 'account_invoice'

     price = fields.Float(compute='_compute_price')
     tons = fields.Floar(compute='_compute_tons')


     @api.one
     @api.depends('invoice_line')
     def _compute_price(self):
       self.price=0
       for line in self.invoice_line:
         self.price = line.price_unit
         break

     @api.depends('price','amount_untaxed')
     def _compute_tons(self):
       self.price = amount_untaxed / price
     
