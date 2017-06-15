from openerp import models


class MRPProduction(models.Model):
    _inherit = 'mrp.production'

    def _make_production_produce_line(self, cr, uid, production, context=None):
        production.location_src_id = production.bom_id.location_src_id and production.bom_id.location_src_id.id or production.product_id.property_stock_production.id
        production.location_dest_id = production.bom_id.location_dest_id and production.bom_id.location_dest_id.id or production.location_dest_id.id
        vals = super(MRPProduction, self)._make_production_produce_line(cr, uid, production, context)
        return vals
