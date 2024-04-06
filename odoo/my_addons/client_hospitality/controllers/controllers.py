# -*- coding: utf-8 -*-
# from odoo import http


# class ClientHospitality(http.Controller):
#     @http.route('/client_hospitality/client_hospitality', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/client_hospitality/client_hospitality/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('client_hospitality.listing', {
#             'root': '/client_hospitality/client_hospitality',
#             'objects': http.request.env['client_hospitality.client_hospitality'].search([]),
#         })

#     @http.route('/client_hospitality/client_hospitality/objects/<model("client_hospitality.client_hospitality"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('client_hospitality.object', {
#             'object': obj
#         })
