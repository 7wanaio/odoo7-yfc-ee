# -*- coding: utf-8 -*-
# from odoo import http


# class TripManage(http.Controller):
#     @http.route('/trip_manage/trip_manage', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/trip_manage/trip_manage/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('trip_manage.listing', {
#             'root': '/trip_manage/trip_manage',
#             'objects': http.request.env['trip_manage.trip_manage'].search([]),
#         })

#     @http.route('/trip_manage/trip_manage/objects/<model("trip_manage.trip_manage"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('trip_manage.object', {
#             'object': obj
#         })
