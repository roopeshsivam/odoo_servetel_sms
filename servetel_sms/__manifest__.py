# -*- coding: utf-8 -*-
{
    'name': 'Servetel sms integration',
    'version': "15.0.0.1",
    'description': 'api integration with servetel',
    'author': "Shivani Sujith",
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/servertel.xml',
        'views/company.xml',
        'views/sale.xml'
        ],
    'installable': True,
    'application': True,
    # 'post_init_hook': 'post_init_hook',
}
