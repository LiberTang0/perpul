# -*- coding: utf-8 -*-
{
    'name': "auto_reset_sequence",

    'summary': """
        Auto Reset Sequences Dayly, Monthly or Yearly!""",

    'description': """
        Auto Reset Sequences Dayly, Monthly or Yearly!
    """,

    'author': "Appnext",
    'website': "http://appnxt.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/flectra/flectra/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}    