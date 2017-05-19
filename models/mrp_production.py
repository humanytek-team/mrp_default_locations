from openerp import api, fields, models


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
        if self.bom_id.location_src_id:
            location = self.bom_id.location_src_id
        else:
            if self._context.get('default_picking_type_id'):
                location = self.env['stock.picking.type'].browse(self.env.context['default_picking_type_id']).default_location_dest_id
            if not location:
                location = self.env.ref('stock.stock_location_stock', raise_if_not_found=False)
        return location and location.id or False

    @api.onchange('bom_id')
    def _set_locations(self):
        location = False
        if self.bom_id.location_src_id:
            location = self.bom_id.location_src_id
        else:
            if self._context.get('default_picking_type_id'):
                location = self.env['stock.picking.type'].browse(self.env.context['default_picking_type_id']).default_location_src_id
            if not location:
                location = self.env.ref('stock.stock_location_stock', raise_if_not_found=False)
        self.location_src_id = location and location.id or False

        location = False
        if self.bom_id.location_src_id:
            location = self.bom_id.location_src_id
        else:
            if self._context.get('default_picking_type_id'):
                location = self.env['stock.picking.type'].browse(self.env.context['default_picking_type_id']).default_location_dest_id
            if not location:
                location = self.env.ref('stock.stock_location_stock', raise_if_not_found=False)
        self.location_dest_id = location and location.id or False
