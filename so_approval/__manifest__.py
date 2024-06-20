# -*- coding: utf-8 -*-
{
    'name': "SO Approval",
    'description': 'Sale Order Approval',
    'application': True,
    'depends': ['base', 'sale'],
    'data': ['security/so_approval_security.xml',
             'security/ir.model.access.csv',
             'views/sale_order_views.xml',
             'wizard/mail_compose_message_views.xml']
}
