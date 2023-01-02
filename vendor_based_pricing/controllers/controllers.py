# -*- coding: utf-8 -*-
# from odoo import http


# class VenderBasedPricing(http.Controller):
#     @http.route('/vendor_based_pricing/vendor_based_pricing', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vendor_based_pricing/vendor_based_pricing/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vendor_based_pricing.listing', {
#             'root': '/vendor_based_pricing/vendor_based_pricing',
#             'objects': http.request.env['vendor_based_pricing.vendor_based_pricing'].search([]),
#         })

#     @http.route('/vendor_based_pricing/vendor_based_pricing/objects/<model("vendor_based_pricing.vendor_based_pricing"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vendor_based_pricing.object', {
#             'object': obj
#         })
