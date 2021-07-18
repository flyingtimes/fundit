# -*- coding: utf-8 -*-
from odoo import http


class CgmFund(http.Controller):
    @http.route('/cgm_fund/cgm_fund/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/cgm_fund/cgm_fund/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('cgm_fund.listing', {
             'root': '/cgm_fund/cgm_fund',
             'objects': http.request.env['cgm_fund.cgm_fund'].search([]),
        })

    @http.route('/cgm_fund/cgm_fund/objects/<model("cgm_fund.cgm_fund"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('cgm_fund.object', {
             'object': obj
        })
