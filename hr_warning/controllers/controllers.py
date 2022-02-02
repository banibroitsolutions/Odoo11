# -*- coding: utf-8 -*-
# from odoo import http


# class HrWarning(http.Controller):
#     @http.route('/hr_warning/hr_warning/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_warning/hr_warning/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_warning.listing', {
#             'root': '/hr_warning/hr_warning',
#             'objects': http.request.env['hr_warning.hr_warning'].search([]),
#         })

#     @http.route('/hr_warning/hr_warning/objects/<model("hr_warning.hr_warning"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_warning.object', {
#             'object': obj
#         })
