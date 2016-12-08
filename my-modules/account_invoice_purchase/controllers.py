# -*- coding: utf-8 -*-
from openerp import http

# class AccountInvoicePurchase(http.Controller):
#     @http.route('/account_invoice_purchase/account_invoice_purchase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_invoice_purchase/account_invoice_purchase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_invoice_purchase.listing', {
#             'root': '/account_invoice_purchase/account_invoice_purchase',
#             'objects': http.request.env['account_invoice_purchase.account_invoice_purchase'].search([]),
#         })

#     @http.route('/account_invoice_purchase/account_invoice_purchase/objects/<model("account_invoice_purchase.account_invoice_purchase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_invoice_purchase.object', {
#             'object': obj
#         })