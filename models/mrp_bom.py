from odoo import api, fields, models


class MRPBOM(models.Model):
    _inherit = 'mrp.bom'

    location_src_id = fields.Many2one(
        'stock.location', 'Source Location',
        help="Location where the system will look for components.")
    location_dest_id = fields.Many2one(
        'stock.location', 'Destination Location',
        help="Location where the system will stock the finished products.")
