# -*- coding: utf-8 -*-
from openerp import fields, models, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    order = fields.Many2one('purchase.order')
    contract_type = fields.Selection(readonly=True, related="order.contract_type")
    tons = fields.Float(compute="_compute_tons")

    @api.one
    @api.depends('move_lines')
    def _compute_tons(self):
      self.tons = 0
      for line in self.move_lines:
        self.tons = line.product_uom_qty
        break
    
