from odoo import models, fields

class PurchaseBid(models.Model):
    _name = 'purchase.bid'
    _description = 'Purchase Bid'

    vendor_id = fields.Many2one('res.partner', string="Vendor", required=True)
    price = fields.Float(string="Bid Price", required=True)
    bid_date = fields.Datetime(string="Bid Date", default=fields.Datetime.now)
    rfq_id = fields.Many2one('purchase.order', string="Request for Quotation", ondelete='cascade')
