# -*- coding: utf-8 -*-
# from odoo import http


# class OrderDemo(http.Controller):
#     @http.route('/order_demo/order_demo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/order_demo/order_demo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('order_demo.listing', {
#             'root': '/order_demo/order_demo',
#             'objects': http.request.env['order_demo.order_demo'].search([]),
#         })

#     @http.route('/order_demo/order_demo/objects/<model("order_demo.order_demo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('order_demo.object', {
#             'object': obj
#         })
