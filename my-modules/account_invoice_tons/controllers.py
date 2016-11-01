# -*- coding: utf-8 -*-
from openerp import http

# class AccountInvoiceTons(http.Controller):
#     @http.route('/account_invoice_tons/account_invoice_tons/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_invoice_tons/account_invoice_tons/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_invoice_tons.listing', {
#             'root': '/account_invoice_tons/account_invoice_tons',
#             'objects': http.request.env['account_invoice_tons.account_invoice_tons'].search([]),
#         })

#     @http.route('/account_invoice_tons/account_invoice_tons/objects/<model("account_invoice_tons.account_invoice_tons"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_invoice_tons.object', {
#             'object': obj
#         })