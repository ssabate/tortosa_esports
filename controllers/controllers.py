# -*- coding: utf-8 -*-
from odoo import http

# class Esports(http.Controller):
#     @http.route('/esports/esports/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/esports/esports/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('esports.listing', {
#             'root': '/esports/esports',
#             'objects': http.request.env['esports.esports'].search([]),
#         })

#     @http.route('/esports/esports/objects/<model("esports.esports"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('esports.object', {
#             'object': obj
#         })