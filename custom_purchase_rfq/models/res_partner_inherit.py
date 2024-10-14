from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    supplier = fields.Boolean("Supplier", default=False)
