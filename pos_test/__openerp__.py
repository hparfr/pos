# -*- coding: utf-8 -*-
##############################################################################
#
#    PoS TEST for Odoo
#
##############################################################################

{
    'name': 'PoS Test',
    'summary': 'PoS Test',
    'version': '1.0',
    'category': 'Point Of Sale',
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'license': 'AGPL-3',
    'depends': [
        'point_of_sale',
    ],
    'data': [
        'views/action.xml',
        'views/menu.xml',
        'views/include.xml',
    ],
    'qweb': [
        'static/src/xml/pos_test.xml',
    ],
}
