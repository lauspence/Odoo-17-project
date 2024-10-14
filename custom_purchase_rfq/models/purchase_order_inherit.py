# models/purchase_order_inherit.py
from odoo import models, fields

# Extending the purchase.order model to add multi-vendor functionality
class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    vendor_ids = fields.Many2many(
        'res.partner', 
        string="Vendors", 
        domain=[('supplier', '=', True)]
    )
    
    bid_ids = fields.One2many(
        'purchase.bid', 'rfq_id', 
        string="Bids"
    )
    
    winning_bid_id = fields.Many2one(
        'purchase.bid', 
        string="Winning Bid"
    )

    def confirm_winning_bid(self):
        # Logic for assigning winning bidder to Purchase Order
        self.partner_id = self.winning_bid_id.vendor_id
        self.state = 'purchase'

