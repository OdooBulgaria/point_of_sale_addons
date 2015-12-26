# -*- coding: utf-8 -*-

{
    'name': 'POS Enhancement',
    'version': '1.2',
    'category': 'Point Of Sale',
    'sequence': 3,
    'author': 'Mostafa Mohamed',
    'summary':
        'Print Order Ref On receipt ,'
        'Print the price of Product after and before applying Pricelist'
        'Print The Total Discount of Pricelist'
        'Print cashier name of receipt ,',
    'description': """
Manage several cashiers for each Point Of Sale by printing the name of the cashier on the receipt.
===================================================================================================
Manage several receipts for each Point Of Sale by printing the Order Ref receipt.
===================================================================================================
Print the price of Product after and before applying Pricelist.
===================================================================================================
Print The Total Discount of Pricelist.
===================================================================================================
    """,
    'depends': ["point_of_sale"],
    'data': [
        'security/ir.model.access.csv',
        'pos_enhance_view.xml',
        'views/template.xml',
    ],
    'qweb': [
        'static/src/xml/pos_enhanced.xml',
    ],
    "images": ["static/description/1.jpg",
               "static/description/1.png",
               "static/description/2.png",
               "static/description/3.png",
               "static/description/4.png",
               "static/description/5.png", ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
