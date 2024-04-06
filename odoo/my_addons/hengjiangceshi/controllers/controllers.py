# -*- coding: utf-8 -*-
from odoo import http


class Hengjiangceshi(http.Controller):
    @http.route('/hengjiangceshi/hengjiangceshi', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/hengjiangceshi/hengjiangceshi/objects', auth='public')
    def list(self, **kw):
        return http.request.render('hengjiangceshi.listing', {
            'root': '/hengjiangceshi/hengjiangceshi',
            'objects': http.request.env['hengjiangceshi.hengjiangceshi'].search([]),
        })

    @http.route('/hengjiangceshi/hengjiangceshi/objects/<model("hengjiangceshi.hengjiangceshi"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('hengjiangceshi.object', {
            'object': obj
        })

