from openerp import api, fields, models


class MRPProduction(models.Model):
    _inherit = 'mrp.production'

    def _src_id_default(self):
        default_location_id = self.env['ir.config_parameter'].get_param('mrp_default_locations_settings.default_location_src_id')
        if default_location_id:
            return int(default_location_id)
        else:
            return False

    def _dest_id_default(self):
        default_location_id = self.env['ir.config_parameter'].get_param('mrp_default_locations_settings.default_location_dest_id')
        if default_location_id:
            return int(default_location_id)
        else:
            return False

    location_src_id = fields.Many2one(
        'stock.location',
        string='Raw Materials Location', required=True,
        readonly=True, states={'draft': [('readonly', False)]},
        help="Location where the system will look for components.", default=_src_id_default)

    location_dest_id = fields.Many2one(
        'stock.location',
        string='Raw Materials Location', required=True,
        readonly=True, states={'draft': [('readonly', False)]},
        help="Location where the system will look for components.", default=_dest_id_default)
