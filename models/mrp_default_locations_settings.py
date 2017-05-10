from openerp import api, fields, models


class MRPDefaultLocationsSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _name = 'mrp_default_locations.settings'

    default_location_src_id = fields.Many2one(
        comodel_name="stock.location",
    )

    default_location_dest_id = fields.Many2one(
        comodel_name="stock.location",
    )

    @api.multi
    def set_default_location_src_id(self):
        conf = self.env['ir.config_parameter']
        conf.set_param('mrp_default_locations_settings.default_location_src_id', int(self.default_location_src_id.id))

    @api.multi
    def set_default_location_dest_id(self):
        conf = self.env['ir.config_parameter']
        conf.set_param('mrp_default_locations_settings.default_location_dest_id', int(self.default_location_dest_id.id))
