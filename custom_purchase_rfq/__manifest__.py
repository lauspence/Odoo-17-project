{
    'name': 'Custom Purchase RFQ',
    'version': '1.0',
    'depends': ['purchase'],  # Ensure that this depends on the Purchase app
    'data': [
        'security/purchase_bid_access.xml',
        'views/purchase_order_views.xml',  # Reference to the view XML
    ],
    'description': 'This module extends the purchase order functionality to support multiple vendors and bidding process.',
    'category': 'Purchases',
    'author': 'Your Name',
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
