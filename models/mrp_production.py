from openerp import api, fields, models


class MRPProduction(models.Model):
    _inherit = 'mrp.production'

    def _src_id_default(self):
        return self.bom_id.location_src_id and self.bom_id.location_src_id.id or False

    def _dest_id_default(self):
        return self.bom_id.location_dest_id and self.bom_id.location_dest_id.id or False

    location_src_id = fields.Many2one(
        'stock.location',
        string='Raw Materials Location',
        required=True,
        readonly=True,
        states={'draft': [('readonly', False)]},
        help="Location where the system will look for components.",
        default=_src_id_default)

    location_dest_id = fields.Many2one(
        'stock.location',
        string='Raw Materials Location',
        required=True,
        readonly=True,
        states={'draft': [('readonly', False)]},
        help="Location where the system will look for components.",
        default=_dest_id_default)
