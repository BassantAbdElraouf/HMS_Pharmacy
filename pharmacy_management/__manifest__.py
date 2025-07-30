{
    'name': 'Pharmacy Management',
    'version': '18.0.0.1.0',
    'author': 'Bassant AbdElraouf',
    'category': 'Pharmacy',
    'depends': ['base','sale','stock', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'data/low_stock_cron.xml',
        'views/pharmacy_prescription_view.xml',
        'views/product_template_inherit.xml',
        'views/product_product_view.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
