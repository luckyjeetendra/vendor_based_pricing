# -*- coding: utf-8 -*-
{
    'name': "Vendor Based Pricing",

    'summary': """
        Populate Purchase Order lines/products from Vendor(res.partner).
        """,

    'description': """
        Populate Purchase Order lines/products from Vendor(res.partner).
            ● Add option to add multiple products and quantities on a vendor.
            ● While selecting the vendor on purchase order, get all the selected products and
            quantity from the vendor and create a purchase order line.
            ● For unit price use the below formula,

            Price unit = Average of the last 100 purchase order line’s unit price for a particular
            product that was purchased before from the same vendor.
    """,

    'author': "JKS",
    # 'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory/Purchase',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': ['product', 'purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/purchase.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
