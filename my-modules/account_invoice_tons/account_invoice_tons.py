# -*- coding: utf-8 -*-

from openerp import models, fields, api

class account_invoice_tons(models.Model):
    _inherit = 'account.invoice'

    price = fields.Float(compute='_compute_price')
    tons = fields.Float(compute='_compute_tons')

    contract_type = fields.Selection([
        ('axc', 'AxC'),
        ('pf', 'Precio Fijo'),
        ('pm', 'Precio Maximo'),
        ('pd', 'Precio Despues'),
        ('na', 'No aplica'),
    ], default='na', required=True)

    @api.one
    @api.depends('invoice_line')
    def _compute_price(self):
      self.price=0
      for line in self.invoice_line:
        self.price = line.price_unit
        break

    @api.depends('price','amount_untaxed')
    def _compute_tons(self):
      if self.price > 0:
        self.tons = self.amount_untaxed /self. price
     
