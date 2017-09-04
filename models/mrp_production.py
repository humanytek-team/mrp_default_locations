from odoo import api, fields, models


class MRPProduction(models.Model):
    _inherit = 'mrp.production'

    @api.model
    def _get_default_location_src_id(self):
        location = False
        if self.bom_id.location_src_id:
            location = self.bom_id.location_src_id
        else:
            if self._context.get('default_picking_type_id'):
                location = self.env['stock.picking.type'].browse(self.env.context['default_picking_type_id']).default_location_src_id
            if not location:
                location = self.env.ref('stock.stock_location_stock', raise_if_not_found=False)
        return location and location.id or False

    @api.model
    def _get_default_location_dest_id(self):
        location = False
        if self.bom_id.location_dest_id:
            location = self.bom_id.location_dest_id
        else:
            if self._context.get('default_picking_type_id'):
                location = self.env['stock.picking.type'].browse(self.env.context['default_picking_type_id']).default_location_dest_id
            if not location:
                location = self.env.ref('stock.stock_location_stock', raise_if_not_found=False)
        return location and location.id or False

    @api.depends('bom_id')
    @api.one
    def _compute_src(self):
        self.location_src_id = self.bom_id.location_src_id or self.location_src_id

    @api.depends('bom_id')
    @api.one
    def _compute_dest(self):
        self.location_dest_id = self.bom_id.location_dest_id or self.location_dest_id

    location_src_id = fields.Many2one(
        'stock.location', 'Raw Materials Location',
        default=_get_default_location_src_id,
        readonly=True,  required=True,
        states={'confirmed': [('readonly', False)]},
        help="Location where the system will look for components.",
        compute='_compute_src',
        store=True,
    )
    location_dest_id = fields.Many2one(
        'stock.location', 'Finished Products Location',
        default=_get_default_location_dest_id,
        readonly=True,  required=True,
        states={'confirmed': [('readonly', False)]},
        help="Location where the system will stock the finished products.",
        compute='_compute_dest',
        store=True,
    )
