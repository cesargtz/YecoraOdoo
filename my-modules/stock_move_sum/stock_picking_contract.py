# -*- coding: utf-8 -*-
from openerp import fields, models, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'


    contract_id = fields.Many2one('purchase.order')
    contract_type = fields.Selection(readonly=True, related="contract_id.contract_type")
    
    
