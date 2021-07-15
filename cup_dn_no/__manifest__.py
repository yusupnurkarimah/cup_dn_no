# -*- coding: utf-8 -*-
{
    'name': "cup_dn_no",

    'summary': """
        Add No DN From SO to Invoice""",

    'description': """
        Add No DN From SO to Invoice
    """,

    'license': "LGPL-3",
    'images': ['static/description/cupdev2.png'],
    'author': "Yusup Nur Karimah",
    'website': "https://yusupnurkarimah.github.io/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
}