# -*- coding: utf-8 -*-
# from odoo import http


# class DevelopList(http.Controller):
#     @http.route('/develop_list/develop_list', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/develop_list/develop_list/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('develop_list.listing', {
#             'root': '/develop_list/develop_list',
#             'objects': http.request.env['develop_list.develop_list'].search([]),
#         })

#     @http.route('/develop_list/develop_list/objects/<model("develop_list.develop_list"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('develop_list.object', {
#             'object': obj
#         })
